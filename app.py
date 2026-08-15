import streamlit as st
from indexing import get_transcript, split_text, create_embeddings, build_vectorstore
from rag_chain import answer_question

st.set_page_config(
    page_title="YouTube RAG Chatbot",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
    .stButton > button {
        background-color: #ff0000;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
    .answer-box {
        background-color: #1a1a1a;
        border-left: 4px solid #ff0000;
        padding: 1.2rem;
        border-radius: 8px;
        color: #f0f0f0;
        margin-top: 1rem;
    }
    .chunk-box {
        background-color: #1a1a1a;
        border: 1px solid #333;
        padding: 0.8rem;
        border-radius: 6px;
        color: #aaa;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🎬 YouTube RAG Chatbot")
st.markdown("*Ask anything about any YouTube video — powered by RAG + Groq*")
st.divider()

# Session State
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "transcript" not in st.session_state:
    st.session_state.transcript = None
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    st.divider()

    video_id_input = st.text_input(
        "🔗 YouTube Video ID",
        placeholder="e.g. x0W2ZbWDQmE"
    )

    language = st.radio(
        "🌐 Transcript Language",
        options=["English", "Hindi"],
        index=0,
        horizontal=True
    )
    lang_code = "en" if language == "English" else "hi"

    load_btn = st.button("🚀 Load Video & Build RAG")

    if st.session_state.video_loaded:
        st.divider()
        st.markdown("### 📊 Stats")
        st.markdown(f"**Chunks:** {len(st.session_state.chunks)}")
        st.markdown(f"**Words:** {len(st.session_state.transcript.split())}")
        st.divider()
        if st.button("🔄 Reset"):
            st.session_state.vectorstore = None
            st.session_state.transcript = None
            st.session_state.chunks = []
            st.session_state.chat_history = []
            st.session_state.video_loaded = False
            st.rerun()

    st.divider()
    st.markdown("**How to use:**")
    st.markdown("1. Paste Video ID\n2. Choose language\n3. Click Load\n4. Ask questions!")
    st.markdown("---")
    st.markdown("Built by **Abdul Samad** 🚀")

# Load Video
if load_btn:
    if not video_id_input.strip():
        st.error("Please enter a YouTube Video ID.")
    else:
        with st.spinner("📥 Fetching transcript..."):
            try:
                transcript = get_transcript(video_id_input.strip(), lang_code)
                st.session_state.transcript = transcript
            except ValueError as e:
                st.error(str(e))
                st.stop()

        with st.spinner("✂️ Splitting into chunks..."):
            chunks = split_text(transcript)
            st.session_state.chunks = chunks

        with st.spinner("🧠 Building vector store..."):
            embeddings = create_embeddings()
            vectorstore = build_vectorstore(chunks, embeddings)
            st.session_state.vectorstore = vectorstore

        st.session_state.video_loaded = True
        st.session_state.chat_history = []
        st.success(f"✅ Done! {len(chunks)} chunks created. Ask your questions!")
        st.rerun()

# Chat Area
if st.session_state.video_loaded:

    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.markdown(
                f'<div class="answer-box">{chat["answer"]}</div>',
                unsafe_allow_html=True
            )

    question = st.chat_input("Ask anything about the video...")

    if question:
        with st.chat_message("user"):
            st.write(question)

        with st.spinner("🔍 Searching & generating answer..."):
            result = answer_question(
                question,
                st.session_state.vectorstore,
                lang_code
            )

        with st.chat_message("assistant"):
            st.markdown(
                f'<div class="answer-box">{result["answer"]}</div>',
                unsafe_allow_html=True
            )
            with st.expander("📄 Source Chunks from Video"):
                for i, chunk in enumerate(result["source_chunks"]):
                    st.markdown(
                        f'<div class="chunk-box"><strong style="color:#ff0000">Chunk {i+1}</strong><br>{chunk}</div>',
                        unsafe_allow_html=True
                    )

        st.session_state.chat_history.append({
            "question": question,
            "answer": result["answer"]
        })

else:
    st.markdown("""
    <div style='text-align:center; padding: 4rem 0; color: #555;'>
        <h1 style='font-size:4rem;'>🎬</h1>
        <h3 style='color:#888'>No video loaded yet</h3>
        <p>Paste a YouTube Video ID in the sidebar and click Load Video</p>
    </div>
    """, unsafe_allow_html=True)