from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def answer_question(question, vectorstore, language="en"):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    lang_instruction = (
        "Answer in English." if language == "en"
        else "Answer in Hindi."
    )

    prompt = f"""
Answer the question using only the provided context.
If the answer is not in the context, say "I could not find this in the video."
{lang_instruction}

Context:
{context}

Question:
{question}

Answer:"""

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
    )
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "source_chunks": [doc.page_content for doc in docs]
    }