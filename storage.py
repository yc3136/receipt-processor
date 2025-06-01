from uuid import uuid4

# dictionary to store points for each receipt ID
_receipt_store = {}

def store_receipt(points: int, data: dict) -> str:
    receipt_id = str(uuid4())
    _receipt_store[receipt_id] = points, data
    return receipt_id

def get_points(receipt_id: str) -> int | None:
    return _receipt_store.get(receipt_id)[0]

def get_receipt(receipt_id: str) -> dict | None:
    return _receipt_store.get(receipt_id)[1]

    