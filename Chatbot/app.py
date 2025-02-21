import streamlit as st
import asyncio

from utils.data_stream import streamer  # Pastikan fungsi streamer ada di modul ini
from langchain_helper import chatbot

def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state.history = []

initialize_session_state()


def on_click_callback():
    human_prompt = st.session_state.human_prompt
    st.session_state.history.append(human_prompt)


st.title('Tax:red[Twelve]')
st.markdown("<style>h1 {text-align: center;}</style>", unsafe_allow_html=True)

chat_placeholder = st.container()
prompt_placeholder = st.form('chat-form')

with chat_placeholder:
    for chat in st.session_state.history:
        st.markdown(chat)

with prompt_placeholder:
    cols = st.columns((6,1))
    cols[0].text_input(
        'Chat',
        value='Hello Bot'
    )

user_input = st.chat_input("Say something")

# if user_input:
#     # Tampilkan pesan pengguna satu kali
#     with st.chat_message("user"):
#         st.write(user_input)
#
#     # Panggil fungsi chatbot secara asynchronous
#     chats = asyncio.run(chatbot(str(user_input)))
#
#     # Tampilkan setiap pesan balasan asisten secara berurutan
#     for i, chat in enumerate(chats):
#         with st.chat_message("assistant"):
#             # Jika pesan terakhir, gunakan streaming untuk efek pengetikan
#             if i == len(chats) - 1:
#                 st.write_stream(streamer(chat[1]))
#             else:
#                 st.write(chat[1])
