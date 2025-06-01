from flask import Flask, request, jsonify
from pydantic import ValidationError
from models import Receipt
from processor import calculate_points
from storage import store_receipt, get_points, get_receipt

app = Flask(__name__)

@app.route("/receipts/process", methods = ["POST"])
def process_receipt():
    try:
        data = request.get_json()
        receipt = Receipt(**data)
        points = calculate_points(receipt)
        receipt_id = store_receipt(points, data)
        return jsonify({"id": receipt_id})
    except ValidationError as e:
        return jsonify({"error": "Invalid input. Please verify.", "details:": e.errors()}), 400
    except Exception as e:
        print("Unhandled server error:", e)
        return jsonify({"error": "Internal server error."}), 500

@app.route("/receipts/<receipt_id>/points", methods = ["GET"])
def receipt_points(receipt_id):
    points = get_points(receipt_id)
    if points is None:
        return jsonify({"error": "No receipt found for the given ID."}), 404
    return jsonify({"points": points})

# my own method: retrieve receipt data with receipt ID
@app.route("/receipts/<receipt_id>/data", methods = ["GET"])
def view_receipt(receipt_id):
    receipt = get_receipt(receipt_id)
    if receipt is None:
        return jsonify({"error": "No receipt found for the given ID."}), 404
    return jsonify(receipt)

if __name__ == "__main__":
    app.run(debug = True)