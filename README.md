# Financial Analytics Backend

A RESTful backend application built with **FastAPI** and **DuckDB** for uploading, storing, querying, and analyzing financial datasets. The application supports CSV/XLSX file ingestion, dataset exploration, metadata extraction, schema inspection, SQL query execution, and basic analytics through a clean, modular backend architecture.

---

## Features

- Upload CSV and Excel (.xlsx) datasets
- Store uploaded datasets in DuckDB
- Preview uploaded records
- Retrieve dataset metadata
- View table schema
- Generate dashboard statistics
- Execute custom SQL queries
- Ask analytical questions through an API endpoint
- Interactive API documentation using Swagger UI

---

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- DuckDB

### Data Processing
- Pandas
- OpenPyXL

### API Testing
- Swagger UI
- Postman

### Version Control
- Git
- GitHub

---

## Project Architecture

```
                Client
                   │
                   ▼
              FastAPI APIs
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
  Routes       Services      Models
                   │
                   ▼
               DuckDB Database
                   │
                   ▼
             JSON Response
```

---

## Project Structure

```
Financial-Analytics-Backend
│
├── app
│   ├── database
│   │   └── db.py
│   │
│   ├── models
│   │   ├── ask_model.py
│   │   └── query_model.py
│   │
│   ├── routes
│   │   ├── upload.py
│   │   ├── preview.py
│   │   ├── metadata.py
│   │   ├── schema.py
│   │   ├── dashboard.py
│   │   ├── query.py
│   │   └── ask.py
│   │
│   ├── services
│   │   ├── file_service.py
│   │   ├── metadata_service.py
│   │   ├── schema_service.py
│   │   ├── dashboard_service.py
│   │   ├── query_service.py
│   │   └── ask_service.py
│   │
│   ├── config.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload CSV/XLSX dataset |
| GET | `/preview` | Preview first five records |
| GET | `/metadata` | Retrieve dataset metadata |
| GET | `/schema` | View dataset schema |
| GET | `/dashboard` | Generate dataset summary |
| POST | `/query` | Execute SQL queries |
| POST | `/ask` | Query the dataset using natural language |

---

## API Workflow

```
Upload Dataset
       │
       ▼
Read using Pandas
       │
       ▼
Store in DuckDB
       │
       ▼
Expose REST APIs
       │
       ├── Preview
       ├── Metadata
       ├── Schema
       ├── Dashboard
       ├── SQL Query
       └── Ask
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/DyutiSaini/financial-analytics-backend.git
```

Navigate to the project directory

```bash
cd financial-analytics-backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the application

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Example SQL Query

```sql
SELECT * FROM uploaded_data_table LIMIT 5;
```

---

## Future Improvements

- Support multiple uploaded datasets
- AI-powered natural language to SQL generation
- Interactive dashboard visualizations
- Authentication and role-based access
- Export analytics reports

---

## Author

**Dyuti Saini**

B.Tech Computer Science Engineering (Artificial Intelligence)

Indira Gandhi Delhi Technical University for Women (IGDTUW)

GitHub: https://github.com/DyutiSaini
