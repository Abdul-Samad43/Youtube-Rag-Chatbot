from langchain_text_splitters import RecursiveCharacterTextSplitter
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

def get_transcript(video_id, language="en"):
    api = YouTubeTranscriptApi()
    lang_codes = ["en", "en-US", "en-GB"] if language == "en" else ["hi", "hi-IN"]
    try:
        transcript = api.fetch(video_id, languages=lang_codes)
    except Exception:
        raise ValueError(
            f"No {'English' if language == 'en' else 'Hindi'} transcript found. "
            "Try switching language or use a different video."
        )
    text = " ".join([snippet.text for snippet in transcript])
    return text

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return chunks

def create_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )
    return embeddings

def build_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )
    vectorstore.save_local("faiss_index")
    return vectorstore