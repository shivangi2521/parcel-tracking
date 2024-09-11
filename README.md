# Tracking Number Generator API

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/shivangi2521/parcel-tracking.git
    cd parcel-tracking
    ```
  
2. Create and Activate a Virtual Environment (Linux):
   
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```


3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Generate Tracking Number

- **URL:** `/api/track/next-tracking-number`
- **EX:** `http://127.0.0.1:8000/api/next-tracking-number`
- **Method:** `GET`
- **Query Parameters:**
  - `origin_country_id`: (string)
  - `destination_country_id`: (string)
  - `weight`: (float)
  - `created_at`: (datetime)
  - `customer_id`: (UUID, required)
  - `customer_name`: (string)
  - `customer_slug`: (string)

- **Response:**
  ```json
  {
    "tracking_number": "PUC4MKZWBJDDUKNS",
    "created_at": "2024-09-11T09:00:53.316016Z",
    "customer_id": "de619854-b59b-425e-9db4-943979e1bd4b",
    "origin_country_id": "US",
    "destination_country_id": "IN",
    "weight": "1.230",
    "customer_name": "john",
    "customer_slug": "john-doe"
  }
