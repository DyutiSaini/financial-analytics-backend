# Financial Analytics Backend

A production-style **AI-powered Financial Analytics Backend** built using **FastAPI**, **DuckDB**, **Pandas**, and **Google Gemini AI**.

The application enables users to upload financial datasets, perform automated data profiling, execute SQL queries, generate charts, analyze datasets, and obtain AI-generated business insights through REST APIs.

---

# Features

### Dataset Management

- Upload CSV and Excel (.xlsx) datasets
- Store uploaded datasets in DuckDB
- Preview uploaded records
- Retrieve dataset metadata
- View dataset schema

---

### Data Analytics

- Dataset Overview
- Numeric Analysis
- Categorical Analysis
- Missing Value Analysis
- Outlier Detection (IQR Method)
- Correlation Analysis
- Dashboard Statistics

---

### Data Visualization

Automatically generates:

- Histograms
- Box Plots
- Bar Charts
- Pie Charts
- Correlation Heatmaps (when applicable)

Charts are generated automatically based on the uploaded dataset.

---

### AI Features

- Automatic Prompt Generation
- AI-powered Dataset Analysis using **Google Gemini 2.5 Flash**
- Executive Summary
- Key KPIs
- Business Insights
- Trends
- Risks
- Recommendations
- Final Conclusion

---

### Querying

- Execute Custom SQL Queries
- Natural Language Questions
- SQL Generation
- Query Execution on DuckDB

---

### API Documentation

- Interactive Swagger UI
- OpenAPI Documentation
- RESTful API Design

---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- DuckDB

## Data Processing

- Pandas
- NumPy
- OpenPyXL

## Visualization

- Matplotlib
- Seaborn

## AI

- Google Gemini 2.5 Flash API

## API Testing

- Swagger UI
- Postman

## Version Control

- Git
- GitHub

---

# Project Architecture

```
                    Client
                       │
                       ▼
              FastAPI REST APIs
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      Routes        Services      Models
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      DuckDB      Analytics     Charts
          │            │            │
          └────────────┼────────────┘
                       ▼
               Prompt Generator
                       │
                       ▼
                 Google Gemini AI
                       │
                       ▼
             Business Insights (JSON)
```

---

# Project Structure

```
Financial-Analytics-Backend
│
├── app
│   │
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
│   │   ├── ask.py
│   │   └── analysis.py
│   │
│   ├── services
│   │   ├── upload_service.py
│   │   ├── file_service.py
│   │   ├── metadata_service.py
│   │   ├── schema_service.py
│   │   ├── dashboard_service.py
│   │   ├── query_service.py
│   │   ├── ask_service.py
│   │   ├── analysis_service.py
│   │   ├── chart_service.py
│   │   ├── prompt_service.py
│   │   └── ai_service.py
│   │
│   ├── config.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# API Endpoints

## Dataset APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/upload` | Upload CSV/XLSX dataset |
| GET | `/preview` | Preview uploaded records |
| GET | `/metadata` | Dataset metadata |
| GET | `/schema` | Dataset schema |
| GET | `/dashboard` | Dataset dashboard |

---

## Query APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/query` | Execute SQL Query |
| POST | `/ask` | Ask Natural Language Questions |

---

## Analysis APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/analysis` | Dataset Overview |
| GET | `/analysis/numeric` | Numeric Summary |
| GET | `/analysis/categorical` | Categorical Summary |
| GET | `/analysis/missing` | Missing Value Report |
| GET | `/analysis/correlation` | Correlation Matrix |
| GET | `/analysis/outliers` | Outlier Report |
| GET | `/analysis/charts` | Generate Charts |
| GET | `/analysis/prompt` | Generate AI Prompt |
| GET | `/analysis/ai` | AI Financial Analysis |

---

# Application Workflow

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
Generate Metadata
      │
      ▼
Perform Analytics
      │
      ├── Dataset Overview
      ├── Numeric Analysis
      ├── Categorical Analysis
      ├── Missing Values
      ├── Outlier Detection
      ├── Correlation
      └── Charts
              │
              ▼
      Build AI Prompt
              │
              ▼
      Google Gemini API
              │
              ▼
      Business Insights (JSON)
```

---

# Installation

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

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Start the server

```bash
python -m uvicorn app.main:app --reload
```

---

# API Documentation

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Example SQL Query

```sql
SELECT * FROM uploaded_data_table LIMIT 10;
```

---

# Example AI Output

The AI endpoint returns structured business insights in JSON format including:

- Executive Summary
- Key KPIs
- Important Trends
- Outliers & Anomalies
- Data Quality Issues
- Business Insights
- Recommendations
- Risks
- Final Conclusion

---

# Future Improvements

- Interactive Frontend Dashboard (React)
- Multiple Dataset Support
- Authentication & Authorization
- Role-Based Access Control
- Download Analytics Reports (PDF/Excel)
- Docker Deployment
- Cloud Deployment (AWS/Azure/GCP)
- Vector Database Integration
- Multi-LLM Support
- Streaming AI Responses

---

# Author

**Dyuti Saini**

B.Tech Computer Science Engineering (Artificial Intelligence)

Indira Gandhi Delhi Technical University for Women (IGDTUW)

GitHub: https://github.com/DyutiSaini

---

# If you found this project useful, consider giving it a star.
