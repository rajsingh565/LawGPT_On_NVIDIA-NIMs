import streamlit as st
import requests
import os

# Configuration for NVIDIA NIMs LLM
# Replace with your actual API key, base URL, and model name
API_KEY = "Your API_KEY"
BASE_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL_NAME = "meta/llama-3.1-8b-instruct"

def generate_legal_response(question):
    """
    Generate a response from the LLM hosted on NVIDIA NIMs.
    Assumes the API is compatible with OpenAI-style chat completions.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    # Enhanced system prompt for more unique and law-specific responses
    system_prompt = (
        "You are LawGPT, a highly knowledgeable legal assistant specializing in Indian law and global law. "
        "Provide detailed, accurate, and context-aware responses to legal questions. "
        "Use legal terminology appropriately and cite relevant laws or sections when possible. "
        "Ensure the answers are unique, insightful, and helpful for legal understanding."
    )
    data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "max_tokens": 700,
        "temperature": 0.6
    }
    try:
        response = requests.post(BASE_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Streamlit UI
st.title("LawGPT: Legal Assistant")

st.write("Ask any legal question related to Indian law (or global law if specified), and get accurate, reliable legal information to assist you.")

question = st.text_input("Enter your legal question:", placeholder="e.g., What are the rights of a tenant in India?")

if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Generating response..."):
            answer = generate_legal_response(question)
        st.subheader("LawGPT's Response:")
        st.write(answer)
    else:
        st.error("Please enter a question.")

