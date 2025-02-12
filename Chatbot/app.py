import streamlit as st
import asyncio

from utils.data_stream import streamer  # Pastikan fungsi streamer ada di modul ini
from langchain_helper import chatbot

st.title('Tax:red[Twelve]')
st.markdown("<style>h1 {text-align: center;}</style>", unsafe_allow_html=True)

user_input = st.chat_input("Say something")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    # Memanggil fungsi chatbot secara asynchronous
    chats = asyncio.run(chatbot(str(user_input)))

    # Tampilkan setiap pesan dalam chat
    for i, chat in enumerate(chats):

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            # Jika pesan terakhir, tampilkan dengan streaming
            if i == len(chats) - 1:
                st.write_stream(streamer(chat[1]))
            else:
                st.write(chat[1])
