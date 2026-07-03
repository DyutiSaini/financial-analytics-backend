from app.database.db import connection
import pandas as pd

def get_schema():

    columns = connection.execute("""
        DESCRIBE uploaded_data_table
    """).fetchdf()

    sample_rows = connection.execute("""
        SELECT *
        FROM uploaded_data_table
        LIMIT 5
    """).fetchdf()

    # Replace NaN values so JSON serialization works
    columns = columns.fillna("")
    sample_rows = sample_rows.fillna("")

    return {
        "columns": columns.to_dict(orient="records"),
        "sample_rows": sample_rows.to_dict(orient="records")
    }