from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os
from app.auth import create_token, verify_token

app = FastAPI(title="Auth Service")

def get_db():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login(data: LoginRequest):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    cur.execute("SELECT password FROM users WHERE username=%s", (data.username,))
    row = cur.fetchone()

    if not row:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (data.username, data.password)
        )
        conn.commit()
    elif row[0] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(data.username)

    cur.close()
    conn.close()

    return {"token": token}

@app.post("/verify")
def verify(token: str):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": user}
