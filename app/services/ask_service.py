from app.database.db import connection

def ask_question(question):

    question = question.lower()

    if "first" in question or "top" in question:

        sql = "SELECT * FROM uploaded_data_table LIMIT 5"

    elif "count" in question or "rows" in question:

        sql = "SELECT COUNT(*) AS total_rows FROM uploaded_data_table"

    elif "columns" in question:

        sql = "DESCRIBE uploaded_data_table"

    else:

        return {
            "message": "Question not supported yet."
        }

    result = connection.execute(sql).fetchdf()

    return {
        "question": question,
        "sql": sql,
        "result": result.to_dict(orient="records")
    }