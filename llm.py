import google.generativeai as genai

genai.configure(api_key="AIzaSyCIZM6jgB9QWd-Ln_s-RlBGqyz7SRb41a8")
#To indentify the versions
#for m in genai.list_models():
#    print(m.name, m.supported_generation_methods)

model=genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(context,question):
    prompt=f"""
You are a helpful assistant.

Use ONLY the context below to answer

Context:
{context}

Question:
{question}
"""
    response=model.generate_content(prompt)

    return response.text