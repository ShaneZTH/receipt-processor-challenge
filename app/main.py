from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/receipts/process")
def process_receipt_endpoint(receipt):
    pass

@app.get("/receipts/{receipt_id}/points")
def get_points_endpoint(receipt_id):
    pass
