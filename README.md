# 🎓 Campus Buddy Bot

> A friendly AI chatbot that helps answer questions about your campus using a local language model and semantic search.

![Campus Buddy Bot Screenshot](static/avatar.png)

## 🧠 Overview

Campus Buddy Bot is a chatbot built with **Streamlit** that uses **local LLM inference** via `llama-cpp-python` and semantic search with `sentence-transformers`. It answers student queries based on a custom knowledge base (`campus_data.json`) — all running **offline** using a **TinyLlama GGUF model**.

---

## 🚀 Features

- ✅ Chat interface with persistent history  
- ✅ Local model inference (no API keys required)  
- ✅ Semantic question matching (handles rephrased/typo'd questions)  
- ✅ Custom avatar and styled UI  
- ✅ Campus-specific knowledge base

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Zainab343/Campus-buddy-bot.git
cd Campus-buddy-bot
