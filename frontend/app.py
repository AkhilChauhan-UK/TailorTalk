import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk AI Booking Assistant")
st.title("TailorTalk 🎓 AI Booking Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Say something:")

if user_input:
    st.session_state.chat.append(("You", user_input))

    try:
        res = requests.post("http://localhost:8000/chat", json={"message": user_input})
        
        # Check for response content type and handle potential non-JSON responses
        if res.status_code != 200:
            st.error(f"Server error: {res.status_code}")
            st.text(res.text)
        else:
            try:
                reply = res.json().get("response")
                st.session_state.chat.append(("TailorTalk", reply))
            except requests.exceptions.JSONDecodeError:
                st.error("Server did not return valid JSON.")
                st.text(res.text)

    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to server.")
        st.text(str(e))

for speaker, msg in st.session_state.chat:
    st.markdown(f"**{speaker}:** {msg}")
