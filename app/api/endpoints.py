from fastapi import APIRouter, HTTPException, Path
from uuid import uuid4
from app.models import Receipt
from app.storage import ReceiptStorage
from app.services import calculate_points

router = APIRouter()
storage = ReceiptStorage()

@router.post("/receipts/process", response_model=dict)
def process_receipt(receipt: Receipt):
    """
    Endpoint to process a receipt and calculate points.
    """
    receipt_id = str(uuid4())
    points = calculate_points(receipt)
    storage.save_receipt(receipt_id, {"receipt": receipt, "points": points})
    return {"id": receipt_id}

@router.get("/receipts/{id}/points", response_model=dict)
def get_points(id: str = Path(..., regex=r"^\S+$")):
    """
    Endpoint to retrieve points for a given receipt ID.
    """
    receipt_data = storage.get_receipt(id)
    if not receipt_data:
        raise HTTPException(status_code=404, detail="No receipt found for that id")
    return {"points": receipt_data["points"]}
