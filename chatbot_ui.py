"""
Project 1 (Generative AI Track): Custom AI Chatbot with Memory
DecodeLabs - Industrial Training Kit
[Streamlit UI version]

This is the WEB "face" of the chatbot. It only handles the page
layout and chat display -- all the actual AI/memory logic lives
in bot_engine.py and is imported from there (same engine used by
the terminal version, chatbot_gemini_memory.py).
"""

import streamlit as st
from bot_engine import MODEL_NAME, make_user_message, make_model_message, get_model_response, trim_history

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Chatbot with Memory",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot with Memory")
st.caption("Project 1 — Generative AI Track · Powered by Gemini")


# ---------------------------------------------------
# MEMORY: In-memory history array
# (stored in Streamlit's session_state so it survives
#  between reruns of the script, but resets on refresh)
# ---------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------------------------------
# SIDEBAR: Controls
# ---------------------------------------------------
with st.sidebar:
    st.header("Settings")
    st.write(f"**Model:** {MODEL_NAME}")
    st.write(f"**Messages in memory:** {len(st.session_state.history)}")
    if st.button("🗑️ Clear conversation"):
        st.session_state.history = []
        st.rerun()


# ---------------------------------------------------
# DISPLAY: Show past messages in a chat layout
# ---------------------------------------------------
for message in st.session_state.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)


# ---------------------------------------------------
# INPUT: Chat input box at the bottom
# ---------------------------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    clean_input = user_input.strip()

    if clean_input == "":
        st.warning("Please type something.")
    else:
        # ---- Show the user's message immediately ----
        with st.chat_message("user"):
            st.markdown(clean_input)

        # ---- Step 1: Append user message to history ----
        st.session_state.history.append(make_user_message(clean_input))

        # ---- Step 2: Ask the engine for a reply ----
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    reply = get_model_response(st.session_state.history)
                except Exception as error:
                    reply = f"Sorry, something went wrong. ({error})"
                    st.session_state.history.pop()
                else:
                    # ---- Step 3: Append model reply to history ----
                    st.session_state.history.append(make_model_message(reply))
                    # ---- Step 4: Keep history within the safe window ----
                    st.session_state.history = trim_history(st.session_state.history)

            st.markdown(reply)