class ReceiptStorage:
    """
    In-memory storage for receipts and associated points.
    Can be swapped with a persistent database or external service.
    """

    def __init__(self):
        self.storage = {}

    def save_receipt(self, receipt_id: str, receipt_data: dict):
        self.storage[receipt_id] = receipt_data

    def get_receipt(self, receipt_id: str):
        return self.storage.get(receipt_id)
