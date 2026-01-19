from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import time

app = FastAPI(title="Payment Service")

class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str = "USD"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/pay")
def process_payment(req: PaymentRequest):
    # Simulate external gateway latency
    time.sleep(random.uniform(0.2, 1.0))

    # Simulate gateway response
    if random.choice([True, True, False]):
        return {
            "order_id": req.order_id,
            "status": "SUCCESS",
            "amount": req.amount,
            "currency": req.currency
        }

    raise HTTPException(
        status_code=502,
        detail="Payment gateway failure"
    )
