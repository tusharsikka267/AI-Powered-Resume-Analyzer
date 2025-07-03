# ResumeMatch.ai – AI‑Powered Resume Analyzer & Job Matcher

A full‑stack Flask application that scores resumes, gives improvement tips using Generative AI, and recommends matching jobs.  
**Stack:** Flask · MongoDB · OpenAI / Sentence‑Transformers · Docker · GitHub Actions · Render (free tier)

## Quick Start (Local)

```bash
git clone https://github.com/yourname/ResumeMatchAI.git && cd ResumeMatchAI
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
export MONGO_URI="mongodb://localhost:27017/resumematch"
python -m spacy download en_core_web_sm
python app.py
```
Open <http://localhost:5000>

## 1‑Click Deploy – Render Free Plan

1. Push the repo to GitHub  
2. Create a **Web Service** on [Render](https://dashboard.render.com)  
3. Select the repo → set environment variables **OPENAI_API_KEY** and **SECRET_KEY**  
4. Build Command: `pip install -r requirements.txt && python -m spacy download en_core_web_sm`  
5. Start Command: `gunicorn -b 0.0.0.0:8000 app:create_app`

## CI/CD with GitHub Actions

The included workflow automatically deploys to Render on push to `main`.

## Folder Structure
```
.
├── app.py
├── utils/
├── models/
├── templates/
├── static/
└── ...
```

## License
MIT
