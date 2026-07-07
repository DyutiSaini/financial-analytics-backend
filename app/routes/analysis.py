from fastapi import APIRouter

from app.services.analysis_service import (
    get_dataset_overview,
    get_missing_value_report,
    get_numeric_summary,
    get_categorical_summary,
    get_missing_value_report,
    get_correlation_matrix,
    get_outlier_report
)
from app.services.chart_service import generate_all_charts
from app.services.prompt_service import build_prompt

from app.services.ai_service import analyze_with_gemini

router = APIRouter()


@router.get("/analysis")
def analysis():

    return get_dataset_overview()


@router.get("/analysis/numeric")
def numeric_analysis():

    return get_numeric_summary()

@router.get("/analysis/categorical")
def categorical_analysis():

    return get_categorical_summary()

@router.get("/analysis/missing")
def missing_analysis():

    return get_missing_value_report()

@router.get("/analysis/correlation")
def correlation_analysis():

    return get_correlation_matrix()

@router.get("/analysis/outliers")
def outlier_analysis():

    return get_outlier_report()

@router.get("/analysis/charts")
def charts():

    return generate_all_charts()

@router.get("/analysis/prompt")
def prompt():

    return {
        "prompt": build_prompt()
    }

@router.get("/analysis/ai")
def ai_analysis():

    prompt = build_prompt()

    result = analyze_with_gemini(prompt)

    return result