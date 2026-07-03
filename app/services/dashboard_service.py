from app.database.db import connection

def get_dashboard():

    df = connection.execute("""
        SELECT * FROM uploaded_data_table
    """).fetchdf()

    total_rows = len(df)
    total_columns = len(df.columns)

    numeric_columns = list(df.select_dtypes(include=["number"]).columns)

    categorical_columns = list(
        df.select_dtypes(include=["object"]).columns
    )

    missing_values = df.isnull().sum().to_dict()

    return {

        "total_rows": total_rows,

        "total_columns": total_columns,

        "numeric_columns": numeric_columns,

        "categorical_columns": categorical_columns,

        "missing_values": missing_values,

        "sample_kpis": [

            f"{total_rows} Records Uploaded",

            f"{total_columns} Columns Detected",

            f"{len(numeric_columns)} Numeric Columns",

            f"{len(categorical_columns)} Categorical Columns"

        ]
    }