from app.database.db import connection
import os
import shutil
import pandas as pd

UPLOAD_FOLDER = "uploads"
LAST_UPLOADED_FILE = None

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_file(file):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    global LAST_UPLOADED_FILE
    LAST_UPLOADED_FILE = file_path

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:

        # Read CSV
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file_path)

        # Read Excel
        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        # Unsupported file
        else:
            return {
                "message": "Only CSV and Excel (.xlsx) files are supported."
            }

    except Exception as e:

        return {
            "message": "Unable to read uploaded file.",
            "error": str(e)
        }

    # Register dataframe in DuckDB
    connection.register("uploaded_data", df)

    # Replace old table with new uploaded data
    connection.execute("""
    DROP TABLE IF EXISTS uploaded_data_table
    """)

    connection.execute("""
    CREATE TABLE uploaded_data_table AS
    SELECT * FROM uploaded_data
    """)

    return {

        "message": "File Uploaded Successfully",

        "filename": file.filename,

        "rows": len(df),

        "columns": list(df.columns)

    }


def get_preview():

    if LAST_UPLOADED_FILE is None:
        return {
            "message": "No file uploaded yet."
        }

    try:

        if LAST_UPLOADED_FILE.endswith(".csv"):
            df = pd.read_csv(LAST_UPLOADED_FILE)

        elif LAST_UPLOADED_FILE.endswith(".xlsx"):
            df = pd.read_excel(LAST_UPLOADED_FILE)

        else:
            return {
                "message": "Unsupported file."
            }

    except Exception as e:

        return {
            "message": "Unable to read file.",
            "error": str(e)
        }

    preview = (
    df.head(5)
      .replace({pd.NA: "", float("nan"): ""})
      .fillna("")
    )

    return {
        "preview": preview.to_dict(orient="records")
    }