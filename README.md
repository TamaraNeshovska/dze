# dze
![DZE Logo](dze_logo1.jpg)
## Project Structure
```bash
dze/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── healthcheck.py       # Each endpoint will have a separate .py file, e.g., home, search, etc.
│   │   ├── schemas/
│   │   │   └── __init__.py          # Pydantic models for request/response
│   │   └── service/
│   │       ├── __init__.py
│   │       └── database.py          # Database connection setup
│   ├── main.py                      # FastAPI app initialization and router inclusion
│   └── dbal.py                       # Database access layer, all DB calls
├── frontend/                         # Frontend project folder
├── README.md                         # Project guidance
├── .env.template                     # Template for environment variables
├── .gitignore                        # Files/folders to ignore in git
└── requirements.txt                  # Python dependencies

```
The following are instructions for setting up and running the Dze backend service.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/TamaraNeshovska/dze.git  or ssh link
cd dze
```
### 1. Run the app locally:
1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate` or `venv/Scripts/Activate.ps1`
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

- Rename .env.template to .env.
- Consult team member to share the file values with you. 

4. Run the API 
locate inside dze/backend and run:

```bash
unicorn main:app --reload
```
-> open unicorn running on http://127.0.0.1:8000  and in the link on the web add /docs as http://127.0.0.1:8000/docs and you will see the fastapi swagger endpoints

5. Run database in docker (install docker fist on your machine if you dont have it, and you can install docker desktop too to see the containers)
```bash
docker compose up -d 
```
- with this you can see all the running containers
```bash
docker ps
```
- run migrations (this will create the initial table with id, location and object)

```bash
python backend/migrations/migration.py

```
