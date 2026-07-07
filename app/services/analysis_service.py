from app.database.db import connection
import pandas as pd
import math

from app.database.db import connection
import pandas as pd


def get_clean_dataframe():

    df = connection.execute("""
        SELECT * FROM uploaded_data_table
    """).fetchdf()

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    return df

def get_dataset_overview():

    df = get_clean_dataframe()

    memory = df.memory_usage(deep=True).sum()

    if memory < 1024 * 1024:
        memory_size = f"{round(memory / 1024, 2)} KB"
    else:
        memory_size = f"{round(memory / (1024 * 1024), 2)} MB"

    overview = {

        "rows": len(df),

        "columns": len(df.columns),

        "duplicates": int(df.duplicated().sum()),

        "missing_values": int(df.isnull().sum().sum()),

        "memory_usage": memory_size

    }

    return overview

def get_numeric_summary():

    df = get_clean_dataframe()

    numeric_df = df.select_dtypes(include="number")

    summary = {}

    for column in numeric_df.columns:

        # Skip empty column
        if numeric_df[column].dropna().empty:
            continue

        # Skip constant column (all values same)
        if numeric_df[column].nunique() <= 1:
            continue

        mean = numeric_df[column].mean()
        median = numeric_df[column].median()
        minimum = numeric_df[column].min()
        maximum = numeric_df[column].max()
        std = numeric_df[column].std()
        variance = numeric_df[column].var()
        q1 = numeric_df[column].quantile(0.25)
        q2 = numeric_df[column].quantile(0.50)
        q3 = numeric_df[column].quantile(0.75)

        summary[column] = {

            "mean": None if pd.isna(mean) else round(float(mean), 2),

            "median": None if pd.isna(median) else round(float(median), 2),

            "min": None if pd.isna(minimum) else float(minimum),

            "max": None if pd.isna(maximum) else float(maximum),

            "std": None if pd.isna(std) else round(float(std), 2),

            "variance": None if pd.isna(variance) else round(float(variance), 2),

            "25%": None if pd.isna(q1) else round(float(q1), 2),

            "50%": None if pd.isna(q2) else round(float(q2), 2),

            "75%": None if pd.isna(q3) else round(float(q3), 2)

        }

    return summary

def get_categorical_summary():

    df = get_clean_dataframe()

    categorical_df = df.select_dtypes(include=["object"])

    summary = {}

    for column in categorical_df.columns:

         # Skip columns having only one unique value
        if categorical_df[column].nunique()<=1:
            continue

        summary[column] = {

            "unique_values": int(categorical_df[column].nunique()),

            "top_value": (
                None
                if categorical_df[column].mode().empty
                else str(categorical_df[column].mode()[0])
            ),

            "frequency": (
                0
                if categorical_df[column].mode().empty
                else int(categorical_df[column].value_counts().iloc[0])
            )

        }

    return summary

def get_missing_value_report():

    df = get_clean_dataframe()

    missing = {}

    for column in df.columns:

        # Skip completely empty columns
        if df[column].isnull().all():
            continue
        count = int(df[column].isnull().sum())

        percentage = round((count / len(df)) * 100, 2)

        missing[column] = {

            "missing_count": count,

            "missing_percentage": percentage

        }

    return missing

def get_correlation_matrix():

    df = get_clean_dataframe()

    numeric_df = df.select_dtypes(include="number")

    numeric_df = numeric_df.loc[:, ~numeric_df.columns.str.contains("^Unnamed")]

    if numeric_df.empty:
        return {
            "message": "No numeric columns found."
        }

    correlation = numeric_df.corr()

    correlation = correlation.fillna(0)

    return correlation.round(2).to_dict()

def get_outlier_report():

    df = get_clean_dataframe()

    numeric_df = df.select_dtypes(include="number")

    summary = {}

    for column in numeric_df.columns:

        # Skip empty numeric columns
        if numeric_df[column].dropna().empty:
            continue

        q1 = numeric_df[column].quantile(0.25)
        q3 = numeric_df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = numeric_df[
            (numeric_df[column] < lower) |
            (numeric_df[column] > upper)
        ]

        summary[column] = {

            "outlier_count": int(len(outliers)),

            "lower_bound": round(float(lower), 2),

            "upper_bound": round(float(upper), 2)

        }

    return summary