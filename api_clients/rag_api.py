import requests

try:
    from config import RAG_API_URL
except:
    RAG_API_URL = None


def ask_rag(question):

    if RAG_API_URL is None:

        return f"""
Demo Mode

Question:
{question}

RAG API not connected yet.
"""

    try:

        response = requests.post(
            RAG_API_URL,
            json={"question": question}
        )

        data = response.json()

        return data.get("answer", "No response")

    except:

        return "API Error"