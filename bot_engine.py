"""
bot_engine.py
DecodeLabs - Project 1 (Generative AI Track)

This is the SHARED "brain" of the chatbot. It knows nothing about
terminals or web pages -- it only knows how to talk to Gemini and
manage conversation memory.

Both chatbot_gemini_memory.py (terminal) and chatbot_ui.py (Streamlit)
import functions from this file instead of duplicating the logic.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_NAME = "gemini-3.6-flash"

MAX_HISTORY_MESSAGES = 20   # sliding window: keeps last 10 exchanges


def make_user_message(text):
    """Wraps plain text into the Content object Gemini expects for a user turn."""
    return types.Content(role="user", parts=[types.Part(text=text)])


def make_model_message(text):
    """Wraps plain text into the Content object Gemini expects for a model turn."""
    return types.Content(role="model", parts=[types.Part(text=text)])


def trim_history(history):
    """
    THE SLIDING WINDOW ALGORITHM (FIFO)
    Returns a trimmed copy of the history list if it has grown past
    the limit, so we don't blow past the model's token budget.
    """
    if len(history) > MAX_HISTORY_MESSAGES:
        overflow = len(history) - MAX_HISTORY_MESSAGES
        return history[overflow:]
    return history


def get_model_response(history):
    """
    Sends the ENTIRE conversation history to Gemini so it has full
    context, and returns just the text of the new reply.
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=history,
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )
    return response.text
