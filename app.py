import streamlit as st
from logic import get_response
import base64
import os

# Set page config
st.set_page_config(page_title="Campus Buddy Bot", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .stTextInput > div > div > input {
            background-color: #2c2c2c;
            color: white;
        }
        .message-bubble {
            padding: 10px 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            max-width: 80%;
        }
        .user {
            background-color: #1f3b70;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .bot {
            background-color: #2c2c2c;
            color: white;
            margin-right: auto;
            text-align: left;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .avatar {
            height: 30px;
            width: 30px;
            border-radius: 50%;
            margin-right: 8px;
            vertical-align: middle;
        }
        .bot-line {
            display: flex;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Convert image to base64 safely
def get_base64_image(path):
    if not os.path.exists(path):
        return ""  # Return empty string if image not found
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

avatar_path = "static/avatar.png"  # Use forward slash for compatibility
avatar_base64 = get_base64_image(avatar_path)

# Header
st.markdown("<h1 style='text-align: center; color: #44ccff;'>🤖 Campus Buddy Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask anything about your campus. I'll try my best to answer!</p>", unsafe_allow_html=True)

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your question:")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    answer = get_response(user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", answer))

# Chat display
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div class='message-bubble user'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='bot-line'>
                {'<img src="data:image/png;base64,' + avatar_base64 + '" class="avatar" />' if avatar_base64 else ''}
                <div class='message-bubble bot'>{msg}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
