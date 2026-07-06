from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random

from rag.loader import extract_text
from rag.chunker import chunk_text
from rag.embeddings import generate_embeddings, model
from rag.retriever import create_faiss_index, retrieve_chunks
from rag.generator import generate_answer
from rag.evaluator import evaluate_answer

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

all_chunks = []


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})


@app.route('/upload', methods=['POST'])
def upload_files():
    global all_chunks

    files = request.files.getlist('files')

    combined_text = ""

    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(file_path)

        extracted_text = extract_text(file_path)

        combined_text += extracted_text + "\n"

    chunks = chunk_text(combined_text)

    embeddings = generate_embeddings(chunks)

    create_faiss_index(embeddings, chunks)

    all_chunks = chunks

    return jsonify({
        "message": "Files uploaded successfully",
        "chunks": len(chunks)
    })


@app.route('/chat', methods=['POST'])
def chat():

    data = request.json

    query = data.get('query')

    top_k = data.get('top_k', 3)

    temperature = data.get('temperature', 0.5)

    query_embedding = model.encode(query)

    retrieved_chunks = retrieve_chunks(query_embedding, top_k)

    if retrieved_chunks == ["No documents uploaded yet."]:
        return jsonify({
            "answer": "Please upload documents first.",
            "sources": []
        })

    answer = generate_answer(
        query,
        retrieved_chunks,
        temperature
    )

    return jsonify({
        "answer": answer,
        "sources": retrieved_chunks
    })


@app.route('/mock-question', methods=['GET'])
def mock_question():

    global all_chunks

    if not all_chunks:
        return jsonify({
            "error": "No uploaded documents found"
        }), 400

    random_chunk = random.choice(all_chunks)

    prompt = f"""
Generate ONE professional interview question from this content.

Content:
{random_chunk}

Rules:
- Only generate ONE question
- No explanation
- No answers
- Keep it concise
"""

    response = generate_answer(
        prompt,
        [random_chunk],
        temperature=0.7
    )

    return jsonify({
        "question": response
    })


@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json

    question = data.get('question')
    answer = data.get('answer')

    evaluation = evaluate_answer(question, answer)

    return jsonify({
        "evaluation": evaluation
    })


if __name__ == '__main__':
    app.run(debug=True)