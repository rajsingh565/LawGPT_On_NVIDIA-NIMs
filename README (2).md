
# LawGPT: Legal Assistant Powered by Generative AI

LawGPT is a Streamlit-based legal assistant that leverages NVIDIA NIMs to provide accurate and context-aware responses to legal questions. It is designed to assist users with queries related to Indian law and global law.

## 🚀 Overview
LawGPT uses a large language model (LLM) hosted on NVIDIA NIMs to generate insightful legal responses. The app features a simple and intuitive interface where users can input legal questions and receive detailed answers.

## 📸 Screenshot
![image_alt](https://github.com/rajsingh565/LawGPT_On_NVIDIA-NIMs/blob/983acd00b45631ad474f713f55b4c0c555eb97ad/Screenshot%202025-09-15%20221841.png)



## ✨ Features
- Streamlit-based user interface
- Integration with NVIDIA NIMs LLM API
- Context-aware responses tailored to Indian and global law
- Legal terminology and citations included when applicable

## 🛠️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lawgpt.git
   cd lawgpt
   ```
2. Install dependencies:
   ```bash
   pip install streamlit requests
   ```
3. Set your NVIDIA NIMs API key and model configuration in the script:
   ```python
   API_KEY = "your-nvidia-api-key"
   BASE_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
   MODEL_NAME = "meta/llama-3.1-8b-instruct"
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📋 Usage
- Enter your legal question in the input box.
- Click "Get Answer" to receive a response from LawGPT.
- Example: `What are the rights of a tenant in India?`

## 🧰 Technologies Used
- [Streamlit](https://streamlit.io/)
- [NVIDIA NIMs](https://developer.nvidia.com/nims)
- [Python](https://www.python.org/)

## 📄 License
This project is licensed under the MIT License.

---
Developed for the Generative AI Challenge: LawGPT on NVIDIA NIMs.
