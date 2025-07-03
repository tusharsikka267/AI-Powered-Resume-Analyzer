import os
import openai
from sentence_transformers import SentenceTransformer, util

openai.api_key = os.getenv("OPENAI_API_KEY")
_embedder = SentenceTransformer("all-MiniLM-L6-v2")

def generate_resume_feedback(parsed_resume: dict) -> str:
    prompt = (
        "You are an expert resume coach. Analyse the following resume "
        "content and give concise, actionable improvement suggestions:\n\n"
        f"{parsed_resume['text']}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

def match_jobs(parsed_resume: dict, jobs_cursor, top_k: int = 5):
    resume_vec = _embedder.encode(" ".join(parsed_resume["skills"]))
    matches = []
    for job in jobs_cursor:
        job_vec = _embedder.encode(job["description"])
        score = util.cos_sim(resume_vec, job_vec).item()
        matches.append((score, job))
    matches.sort(key=lambda x: x[0], reverse=True)
    return [job for score, job in matches[:top_k]]
