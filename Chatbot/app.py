import streamlit as st

from utils.data_stream import streamer

st.title('Tax:red[Twelve]')
st.markdown("<style>h1 {text-align: center;}</style>", unsafe_allow_html=True)

text = 'anuauanunu anuanua fdknsa  aladkf adkfn  aldfknans  fdalsdfn  ndsalkndf  salkndf a nkdasdf lkkn anuauanunu anuanua fdknsa  aladkf adkfn  aldfknans  fdalsdfn  ndsalkndf  salkndf a nkdasdf lkkn anuauanunu anuanua fdknsa  aladkf adkfn  aldfknans  fdalsdfn  ndsalkndf  salkndf a nkdasdf lkkn '

prompt = st.chat_input("Say something")

for i in range(5):
    with st.chat_message("user"):
        st.write(f"Hello 👋 {i}")
        st.write(f"{text}")

    with st.chat_message("assistant"):
        st.write("Hello human")

        if i == 4:
            st.write_stream(streamer(text))

        else:
            st.write(text)

