Vesta Estates - FastAPI Backend (Render-ready)
=============================================

This package is prepared to be deployed to Render (https://render.com).
It connects to your Supabase PostgreSQL via DATABASE_URL.

Quick deploy steps:
1. Create a new GitHub repository and push this project.
2. On Render, create a new Web Service, link the GitHub repo.
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
3. Add the following Environment variables on Render (or let the .env be used locally):
   - DATABASE_URL (your Supabase connection string)
   - SECRET_KEY (your secret key)
   - ALGORITHM=HS256
   - ACCESS_TOKEN_EXPIRE_MINUTES=1440
4. Deploy. Render will install dependencies and start the app.

Local run (for testing):
  python -m venv .venv
  source .venv/bin/activate   # or .venv\Scripts\activate on Windows
  pip install -r requirements.txt
  cp .env.example .env        # then edit .env with your values (or use the provided .env)
  uvicorn main:app --reload --port 8000

NOTE: Do NOT commit .env to public repos. Rotate secrets if shared.
