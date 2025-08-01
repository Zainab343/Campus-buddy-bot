import json
import difflib
from llama_cpp import Llama

# Lazy-load model only once
_llm_instance = None

def get_llm():
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = Llama(
            model_path="models/tinyllama.gguf",
            n_ctx=512,
            n_threads=4
        )
    return _llm_instance

# Load campus Q&A
with open("campus_data.json", "r", encoding="utf-8") as f:
    campus_data = json.load(f)

questions_list = [entry["question"].lower().strip() for entry in campus_data]

def get_similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def match_question(user_input):
    matches = difflib.get_close_matches(user_input.lower().strip(), questions_list, n=1, cutoff=0.6)
    if matches:
        matched = matches[0]
        if get_similarity(user_input, matched) >= 0.75:
            for entry in campus_data:
                if entry["question"].lower().strip() == matched:
                    return entry["answer"]
    return None

SYSTEM_PROMPT = """You are Campus Buddy, an AI chatbot built to help students of Riphah International University.
You answer queries only related to university campuses, admission process, departments, faculty, transport, and location.
If you don't know the answer, say \"I'm not sure, please contact university support.\"."""

def get_response(user_input: str) -> str:
    user_input_lower = user_input.lower().strip()

    # Handle greetings and friendly expressions
    if user_input_lower in ["hi", "hello", "hey", "salam", "assalamualaikum"]:
        return "Hello! I'm Campus Buddy 👋. How can I help you today?"
    if user_input_lower in ["ok", "okay", "okie", "thanks", "thank you"]:
        return "You're welcome! Let me know if there's anything else I can help with."
    if user_input_lower in ["bye", "goodbye", "see you"]:
        return "Goodbye! Feel free to come back if you have more questions."
    if "how are you" in user_input_lower:
        return "I'm just a bot, but I'm here and ready to help you!"

    # Match from dataset
    matched_answer = match_question(user_input)
    if matched_answer:
        return matched_answer

    # No match — reply safely
    return "I'm not sure about that. Please contact university support for more information."
