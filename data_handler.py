import json
import os

# Load campus data
def load_campus_data(file_path="campus_data.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Search for a matching question
def find_answer_in_json(user_question, data):
    user_question = user_question.lower()

    for item in data:
        if item["question"].lower() in user_question:
            return item["answer"]
    
    return None
