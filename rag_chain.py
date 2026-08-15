from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
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

    llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)
    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):
        answer = "".join(
        block.get("text", "")
        for block in answer
        if isinstance(block, dict)
    )

    return {
    "answer": answer,
    "source_chunks": [doc.page_content for doc in docs]
}