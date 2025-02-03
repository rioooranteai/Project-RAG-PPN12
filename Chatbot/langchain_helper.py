import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.chains import (
    StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
)
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI


load_dotenv()

combine_docs_chain = StuffDocumentsChain(...)
vectorstore = ...
retriever = vectorstore.as_retriever()

template = (
    "Combine the chat history and follow up question into "
    "a standalone question. Chat History: {chat_history}"
    "Follow up question: {question}"
)

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))


def chatbot(prompt):
    prompt = PromptTemplate.from_template(template)
    question_generator_chain = LLMChain(llm=llm, prompt=prompt)
    chain = ConversationalRetrievalChain(
        combine_docs_chain=combine_docs_chain,
        retriever=retriever,
        question_generator=question_generator_chain,
    )
    type(chain.memory.buffer)

chatbot("anu")




