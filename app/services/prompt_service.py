from app.services.analysis_service import (
    get_dataset_overview,
    get_numeric_summary,
    get_categorical_summary,
    get_missing_value_report,
    get_outlier_report
)

from app.services.chart_service import generate_all_charts

def build_prompt():
    overview = get_dataset_overview()

    numeric = get_numeric_summary()

    categorical = get_categorical_summary()

    missing = get_missing_value_report()

    outliers = get_outlier_report()

    charts = generate_all_charts()

    prompt = f"""
    You are a Senior Financial Data Analyst.

    Analyze the uploaded dataset using the following information.

    --------------------------------------------------

    DATASET OVERVIEW

    Rows : {overview["rows"]}

    Columns : {overview["columns"]}

    Duplicate Rows : {overview["duplicates"]}

    Missing Values : {overview["missing_values"]}

    Memory Usage : {overview["memory_usage"]}

    --------------------------------------------------

    NUMERIC SUMMARY

    {numeric}

    --------------------------------------------------

    CATEGORICAL SUMMARY

    {categorical}

    --------------------------------------------------

    MISSING VALUE REPORT

    {missing}

    --------------------------------------------------

    OUTLIER REPORT

    {outliers}

    --------------------------------------------------

    CHARTS GENERATED

    {charts}

    --------------------------------------------------

    Return ONLY a valid JSON object.

    Do not return markdown.

    Do not write any explanation before or after the JSON.

    Return the response exactly in this format:

    {{
        "executive_summary": "",

        "key_kpis": [
            "",
            "",
            ""
        ],

        "important_trends": [
            "",
            "",
            ""
        ],

        "outliers_and_anomalies": [
            "",
            ""
        ],

        "data_quality_issues": [
            "",
            ""
        ],

        "business_insights": [
            "",
            "",
            ""
        ],

        "recommendations": [
            "",
            "",
            ""
        ],

        "risks": [
            "",
            ""
        ],

        "final_conclusion": ""
    }}

    Rules:

    - Use only the information available in the dataset.
    - Do not invent facts.
    - Keep each point short and professional.
    - Return valid JSON only.

        """

    return prompt