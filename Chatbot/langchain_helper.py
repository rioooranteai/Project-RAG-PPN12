import os
import asyncio
import warnings

from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.memory import ConversationSummaryBufferMemory

warnings.filterwarnings('ignore')


# Memuat variabel lingkungan
load_dotenv()

# Inisialisasi Pinecone dengan API key dan environment
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment="us-east-1")

# Definisikan model embeddings
model_name = 'intfloat/multilingual-e5-large'
embeddings = HuggingFaceEmbeddings(model_name=model_name)

# Inisialisasi Pinecone vectorstore menggunakan index yang sudah ada
index_name = pc.Index("rag-ppn-12")  # Pastikan index ini sudah dibuat di Pinecone
vectorstore = PineconeVectorStore(index=index_name, embedding=embeddings)

# Membuat retriever dari vectorstore
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Inisialisasi LLM dengan OpenAI API key
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Template untuk memastikan chatbot tidak menjawab jika tidak ada informasi
template = """Gunakan informasi berikut untuk menjawab pertanyaan pengguna.

{context}

Jika tidak ada informasi yang relevan dalam konteks di atas, dan pertanyaannya tidak berkaitan 
dengan pembahasan PPN 12 Persen, katakan:
"Saya tidak memiliki informasi untuk menjawab pertanyaan ini."

Pertanyaan: {question}
Jawaban:"""

prompt_template = PromptTemplate(input_variables=['context', 'question'], template=template)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    input_key='question',
    output_key='answer',
    memory_key='chat_history',
    return_messages=True,
    max_token_limit=1000
)

# Inisialisasi ConversationalRetrievalChain
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,  # Debugging untuk melihat sumber dokumen
    combine_docs_chain_kwargs={"prompt": prompt_template},
    memory=memory
)

# Chat history untuk menyimpan percakapan
chat_history = []

# Fungsi chatbot yang menggabungkan retrieval dan question generation
async def chatbot(prompt):
    context = memory.chat_memory.messages if memory.chat_memory and memory.chat_memory.messages else []
    context_sentence = "\n".join([message.content for message in context]) if context else ""

    result = await chain.ainvoke({"context":context_sentence,
                                  "question":prompt})

    chat_history.append((prompt, result['answer']))

    return chat_history



