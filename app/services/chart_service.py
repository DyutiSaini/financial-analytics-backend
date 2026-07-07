from app.database.db import connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

CHART_FOLDER = "charts"
os.makedirs(CHART_FOLDER, exist_ok=True)


# -----------------------------
# Helper Functions
# -----------------------------
def is_valid_column(column):
    return (
        not str(column).startswith("Unnamed")
    )


def clean_dataframe(df):

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    return df


# -----------------------------
# Histogram
# -----------------------------
def generate_histograms(df):

    chart_paths = []

    numeric_df = df.select_dtypes(include="number")

    for column in numeric_df.columns:

        if numeric_df[column].dropna().empty:
            continue

        if numeric_df[column].nunique() <= 1:
            continue

        plt.figure(figsize=(9,5))

        plt.hist(
            numeric_df[column].dropna(),
            bins=10,
            edgecolor="black"
        )

        plt.title(f"{column} Distribution")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.tight_layout()

        filepath = os.path.join(
            CHART_FOLDER,
            f"hist_{column}.png"
        )

        plt.savefig(filepath)
        plt.close()

        chart_paths.append(filepath)

    return chart_paths


# -----------------------------
# Box Plot
# -----------------------------
def generate_boxplots(df):

    chart_paths = []

    numeric_df = df.select_dtypes(include="number")

    for column in numeric_df.columns:

        if numeric_df[column].dropna().empty:
            continue

        if numeric_df[column].nunique() <= 1:
            continue

        plt.figure(figsize=(6,5))

        plt.boxplot(
            numeric_df[column].dropna()
        )

        plt.title(f"{column} Box Plot")

        plt.tight_layout()

        filepath = os.path.join(
            CHART_FOLDER,
            f"box_{column}.png"
        )

        plt.savefig(filepath)
        plt.close()

        chart_paths.append(filepath)

    return chart_paths


# -----------------------------
# Bar Chart
# -----------------------------
def generate_bar_charts(df):

    chart_paths = []

    categorical_df = df.select_dtypes(include="object")

    for column in categorical_df.columns:

        values = df[column].dropna().value_counts()

        unique = len(values)

        # Skip useless columns
        if unique <= 1:
            continue

        # Too many categories
        if unique > 20:
            continue

        # Pie chart will handle <=6
        if unique <= 6:
            continue

        values = values.head(10)

        plt.figure(figsize=(10,6))

        values.plot(kind="bar")

        plt.title(f"{column}")

        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()

        filepath = os.path.join(
            CHART_FOLDER,
            f"bar_{column}.png"
        )

        plt.savefig(filepath)
        plt.close()

        chart_paths.append(filepath)

    return chart_paths


# -----------------------------
# Pie Chart
# -----------------------------
def generate_pie_charts(df):

    chart_paths = []

    categorical_df = df.select_dtypes(include="object")

    for column in categorical_df.columns:

        values = df[column].dropna().value_counts()

        unique = len(values)

        if unique <= 1:
            continue

        if unique > 6:
            continue

        labels = []

        for label in values.index:

            label = str(label)

            if len(label) > 20:
                label = label[:20] + "..."

            labels.append(label)

        plt.figure(figsize=(10,8))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title(column)

        plt.tight_layout()

        filepath = os.path.join(
            CHART_FOLDER,
            f"pie_{column}.png"
        )

        plt.savefig(filepath)
        plt.close()

        chart_paths.append(filepath)

    return chart_paths


# -----------------------------
# Heatmap
# -----------------------------
def generate_heatmap(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None

    plt.figure(figsize=(10,8))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    filepath = os.path.join(
        CHART_FOLDER,
        "heatmap.png"
    )

    plt.savefig(filepath)
    plt.close()

    return filepath


# -----------------------------
# Master Function
# -----------------------------
def generate_all_charts():

    # Delete old charts
    for file in os.listdir(CHART_FOLDER):

        if file.endswith(".png"):

            os.remove(
                os.path.join(CHART_FOLDER, file)
            )

    df = connection.execute("""
        SELECT * FROM uploaded_data_table
    """).fetchdf()

    df = clean_dataframe(df)

    return {

        "histograms": generate_histograms(df),

        "boxplots": generate_boxplots(df),

        "bar_charts": generate_bar_charts(df),

        "pie_charts": generate_pie_charts(df),

        "heatmap": generate_heatmap(df)

    }