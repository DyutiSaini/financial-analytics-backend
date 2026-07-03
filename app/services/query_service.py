from app.database.db import connection
import pandas as pd


def execute_query(query):

    try:

        result = connection.execute(query).fetchdf()

        # Replace NaN with empty string
        result = result.fillna("")

        return {

            "rows": len(result),

            "result": result.to_dict(orient="records")

        }

    except Exception as e:

        return {

            "message": "Query execution failed.",

            "error": str(e)

        }