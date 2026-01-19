from fastapi import FastAPI
import redis
import os
import json
import time

app = FastAPI(title="Video Service")

REDIS_HOST = os.getenv("REDIS_HOST", "video-redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

VIDEO_DATA = [
    {"id": "v1", "title": "Intro to StreamCart", "url": "https://example.com/v1"},
    {"id": "v2", "title": "Product Demo", "url": "https://example.com/v2"},
    {"id": "v3", "title": "How Payments Work", "url": "https://example.com/v3"},
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/videos")
def get_videos():
    cached = r.get("videos")

    if cached:
        return {
            "source": "cache",
            "data": json.loads(cached)
        }

    # Simulate slow source
    time.sleep(1)

    r.set("videos", json.dumps(VIDEO_DATA), ex=60)

    return {
        "source": "origin",
        "data": VIDEO_DATA
    }
