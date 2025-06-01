# Receipt Processor API

A lightweight web service that processes receipts and awards points based on specific rules.

This project was developed as part of a technical assessment. It includes:
- A RESTful API built with Flask and Pydantic
- In-memory storage (no database required)
- Dockerized setup for easy testing
- Unit tests using `pytest`
- Built and tesed on **Postman**
- Optional bonus endpoint to retrieve original receipt data


## Setup Instructions

### Option 1: Run Locally

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yc3136/receipt-processor.git
   cd receipt-processor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**
   ```bash
   python app.py
   ```
   The API will be available at:  
   `http://127.0.0.1:5000`

---

### Option 2: Run via Docker

1. **Build the container**
   ```bash
   docker build -t receipt-processor .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 receipt-processor
   ```

---

## API Endpoints

### `POST /receipts/process`  
Submit a receipt for processing.

**Request:**
```json
{
  "retailer": "Amazon",
  "purchaseDate": "2025-05-29",
  "purchaseTime": "21:06",
  "items": [
    { "shortDescription": "Bobbie Organic Gentle Baby Formula", "price": "29.99" },
    { "shortDescription": "Pat the Bunny", "price": "16.81" }
  ],
  "total": "46.80"
}
```

**Response:**
```json
{ "id": "7831976f-bb61-4004-92fd-5be02ecdb4ec" }
```

---

### `GET /receipts/{id}/points`  
Return the points awarded to the receipt.

**Response:**
```json
{ "points": 17 }
```

---

### `GET /receipts/{id}/data`  
*Bonus Endpoint* – Retrieve the original receipt by ID.  
Useful for debugging or confirming receipt storage.

---

## Testing

### Run unit tests
```bash
pytest
```

Includes:
- Valid normal, zero-point and maximal-point examples
- Invalid inputs like missing fields and bad formatting
- Bonus: Retrieval endpoint test

---

## Technologies

- **Flask** – lightweight Python web framework
- **Pydantic** – data validation with detailed error messages
- **Pytest** – unit testing
- **Docker** – containerization for consistent environments
- **Postman** – API testing and validation during development

---

## Creative Touch

As an extra feature, I added a `/receipts/{id}/data` endpoint that returns the original receipt data from memory — helpful for confirming submissions during development and testing.

---

## File Structure Overview

```
receipt-processor/
├── app.py               # Main Flask app
├── processor.py         # Business logic (points calculation)
├── storage.py           # In-memory receipt storage
├── models.py            # Pydantic models and validation
├── tests.py             # Unit tests using pytest
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
```

---

## Final Notes

This solution fulfills all requirements and implements an additional API endpoint for retrieving the original receipt data.
Thank you for reviewing!
