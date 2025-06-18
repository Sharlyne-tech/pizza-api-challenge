# Pizza API Challenge

A Flask-based RESTful API for managing pizzas, restaurants, and their relationships.

---

## Project Structure


---

pizza-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── models/
│ └── controllers/
├── venv/
├── requirements.txt
└── README.md

yaml
Copy
Edit


## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd pizza-api-challenge


Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Set environment variables
Create a .flaskenv file in the root directory with:

FLASK_APP=server.app
FLASK_ENV=development



How to Run Locally
Make sure your virtual environment is activated.

If you use database migrations, run:
flask db upgrade


Start the Flask development server:
flask run


Open your browser or API client and navigate to:
http://127.0.0.1:5000/

API Endpoints
/restaurants — CRUD operations for restaurants

/pizzas — CRUD operations for pizzas

/restaurant_pizzas — Manage pizza menus for restaurants


