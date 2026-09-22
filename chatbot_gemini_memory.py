"""
Project 1 (Generative AI Track): Custom AI Chatbot with Memory
DecodeLabs - Industrial Training Kit
[Terminal version]

This is the TERMINAL "face" of the chatbot. It only handles the
input/output loop -- all the actual AI/memory logic lives in
bot_engine.py and is imported from there.
"""

from bot_engine import make_user_message, make_model_message, get_model_response, trim_history

# ---------------------------------------------------
# MEMORY: In-memory history array (lives here, in the "face" file,
# not in the engine -- the engine just operates on whatever list
# you hand it)
# ---------------------------------------------------
conversation_history = []


def main():
    global conversation_history
    print("Chatbot: Hello! I'm an AI assistant with memory (powered by Gemini).")
    print("Chatbot: Type 'bye' or 'exit' anytime to end the chat.\n")

    # ---------------------------------------------------
    # THE HEARTBEAT: Infinite Loop (continuous session)
    # ---------------------------------------------------
    while True:

        # ---- Input & Sanitization ----
        raw_input = input("You: ")
        clean_input = raw_input.strip()

        # ---- Structural Validation Gate ----
        if clean_input == "":
            print("Chatbot: Please type something.")
            continue

        # ---- Exit command ----
        if clean_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        # ---- Step 1: Append the user's message to history ----
        conversation_history.append(make_user_message(clean_input))

        # ---- Step 2: Ask the engine for a reply ----
        try:
            reply = get_model_response(conversation_history)
        except Exception as error:
            print(f"Chatbot: Sorry, something went wrong. ({error})")
            conversation_history.pop()
            continue

        # ---- Step 3: Append the model's response to history ----
        conversation_history.append(make_model_message(reply))

        # ---- Step 4: Keep the history within the token-safe window ----
        conversation_history = trim_history(conversation_history)

        # ---- Output ----
        print(f"Chatbot: {reply}")


if __name__ == "__main__":
    main()