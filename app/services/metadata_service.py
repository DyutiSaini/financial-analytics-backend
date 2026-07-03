from app.database.db import connection

def get_metadata():

    columns = connection.execute("""
        DESCRIBE uploaded_data_table
    """).fetchdf()

    rows = connection.execute("""
        SELECT COUNT(*) FROM uploaded_data_table
    """).fetchone()[0]

    return {
        "rows": rows,
        "columns": columns.to_dict(orient="records")
    }