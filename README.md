# Receipt Processor

This is a Python-based API for processing receipts and calculating reward points based on predefined rules. The API is built with **FastAPI**, ensuring scalability, maintainability, and performance.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Embedded Logic](#embedded-logic)
3. [Installation and Setup](#installation-and-setup)
    - [Dockerized Environment](#dockerized-environment)
    - [Local Environment](#local-environment)
4. [Testing](#testing)

---

## Project Structure

```text
receipt-processor/
│
├── app/
│   ├── api/
│   │   ├── endpoints.py       # API routes (encapsulated endpoints)
│   │   └── __init__.py
│   ├── models.py              # Data models (Pydantic schemas)
│   ├── services.py            # Business logic and point calculation
│   ├── storage.py             # Storage handling (receipt storage abstraction)
│   └── __init__.py
│
├── tests/
│   ├── test_endpoints.py      # Unit tests for API endpoints
│   └── __init__.py
│
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

## Embedded Logic

The receipt processing logic resides in the `services.py` file, and it follows these rules:

1. **Retailer Name**: Add 1 point for every alphanumeric character in the retailer name.
2. **Total Amount**:
   - Add 50 points if the total is a round dollar amount with no cents.
   - Add 25 points if the total is a multiple of 0.25.
3. **Items**:
   - Add 5 points for every two items on the receipt.
   - Add 0.2 points for every dollar of an item’s price if its short description length is a multiple of 3.
4. **Purchase Date**:
   - Add 6 points if the purchase date is even.
5. **Purchase Time**:
   - Add 10 points if the time is between 2:00 PM and 4:00 PM.

These rules are implemented in the `calculate_points()` function.

---

## Installation and Setup

### Dockerized Environment

1. Build the Docker Image:

    ```bash
    docker build -t receipt-processor .
    ```

2. Run the Docker Container:

    ```bash
    docker run -p 8000:8000 receipt-processor
    ```

3. Access the API:

    Open a browser and navigate to: http://localhost:8000/docs to see the Swagger UI documentation.


### **Local Environment**

1. Clone the Repository:

   ```bash
   git clone <repository-url>
   cd receipt-processor
   ```

2. Create and Activate a Virtual Environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Application:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

5. Access the API:
    
    Open a browser and navigate to: http://localhost:8000/docs to see the Swagger UI documentation.


---

## Testing

### Run Unit Tests

To run the included unit tests, use the following command:
```bash
pytest
```