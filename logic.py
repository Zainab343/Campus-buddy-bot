import json
import difflib
from llama_cpp import Llama

# Load your LLM model
MODEL_PATH = "models/tinyllama.gguf"  # Adjust path if needed

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=512,
    n_threads=4
)

# Load predefined campus Q&A data
with open("campus_data.json", "r", encoding="utf-8") as f:
    campus_data = json.load(f)

# Build list of questions for matching
questions_list = [entry["question"].lower().strip() for entry in campus_data]

def match_question(user_input):
    # Use get_close_matches to find a similar question
    matches = difflib.get_close_matches(user_input.lower().strip(), questions_list, n=1, cutoff=0.6)
    if matches:
        matched_question = matches[0]
        for entry in campus_data:
            if entry["question"].lower().strip() == matched_question:
                return entry["answer"]
    return None

# System prompt
SYSTEM_PROMPT = (
    "You are Campus Buddy, a helpful assistant for students at Riphah International University, "
    "Gulberg Greens, Islamabad. Respond concisely and helpfully."
)

def get_response(user_input: str) -> str:
    # Try matching from campus data first
    matched_answer = match_question(user_input)
    if matched_answer:
        return matched_answer

    # Else use LLM
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_input}\nBot:"
    output = llm(prompt, max_tokens=256, stop=["User:"], echo=False)
    return output["choices"][0]["text"].strip() or "I'm not sure about that. Please contact student services."
