from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection
def connect_database():
    engine = create_engine(
        "mysql+pymysql://username:password@localhost/database_name"
    )

    print("Database connected successfully")
    return engine

# Load telecom churn data from MySQL
def load_data(engine):
    query = """
    SELECT
        customerID,
        tenure,
        Contract,
        PaymentMethod,
        TechSupport,
        InternetService,
        MonthlyCharges,
        OnlineBackup,
        Churn_flag
    FROM telco;
    """
    df = pd.read_sql(query, engine)
    print("Data loaded successfully")
    print("Rows:",len(df))
    return df

# Create engineered customer features
def create_features(df):
    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=[
            "0-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49-72 Months"
        ]
    )

    df["charge_group"] = pd.qcut(
        df["MonthlyCharges"],
        q=4,
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )
    print("Features created successfully")
    return df

# Build churn risk score
def build_risk_score(df):
    df["risk_score"] = 0

    df.loc[df["tenure_group"] == "0-12 Months", "risk_score"] += 4
    df.loc[df["Contract"] == "Month-to-month", "risk_score"] += 4
    df.loc[df["TechSupport"] == "No", "risk_score"] += 3
    df.loc[df["InternetService"] == "Fiber optic", "risk_score"] += 3
    df.loc[df["OnlineBackup"] == "No", "risk_score"] += 3
    df.loc[df["PaymentMethod"] == "Electronic check", "risk_score"] += 2
    df.loc[df["charge_group"].isin(["High", "Very High"]), "risk_score"] += 2

    df["risk_category"] = pd.qcut(
        df["risk_score"],
        q=3,
        labels=[
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ]
    )

    print("Risk score created successfully")
    return df

#Validating the scores that are created
def validate(df):
    risk_validation = df.groupby("risk_category")["Churn_flag"].agg(["mean", "count"])
    print("\nRisk Category Validation")
    print(risk_validation)

    score_validation = df.groupby("Churn_flag")["risk_score"].mean()
    print("\nRisk Score Validation")
    print(score_validation)

#Creating charts
def create_charts(df):
    #Chart 1
    risk_plot = (
        df.groupby("risk_category")["Churn_flag"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 5))
    bars = plt.bar(
        risk_plot["risk_category"],
        risk_plot["Churn_flag"]
    )

    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:.2%}",
            ha='center'
        )

    plt.bar(risk_plot["risk_category"], risk_plot["Churn_flag"])
    plt.xlabel("Risk Category")
    plt.ylabel("Churn Rate")
    plt.title("Churn Rate Across Risk Categories")
    plt.savefig("risk_category_churn.png")

    plt.show()

    #Chart 2
    tenure_plot = (
        df.groupby("tenure_group")["Churn_flag"]
        .mean()
        .reset_index()
    )
    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        tenure_plot["tenure_group"],
        tenure_plot["Churn_flag"]
    )
    for bar in bars:
        y = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:.1%}",
            ha='center'
        )

    plt.xlabel("Tenure Group")
    plt.ylabel("Churn Rate")
    plt.title("Churn Rate by Customer Tenure")
    plt.savefig("tenure_churn.png")
    plt.show()

    #Chart 3
    charge_plot = (
        df.groupby("charge_group")["Churn_flag"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 5))
    bars = plt.bar(
        charge_plot["charge_group"],
        charge_plot["Churn_flag"]
    )

    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:.1%}",
            ha="center"
        )

    plt.xlabel("Monthly Charge Group")
    plt.ylabel("Churn Rate")
    plt.title("Churn Rate by Monthly Charge Group")
    plt.savefig("charge_group_churn.png")
    plt.show()

    print("\nCharts created successfully")


def main():
    engine = connect_database()
    df = load_data(engine)
    df = create_features(df)
    df = build_risk_score(df)
    validate(df)
    create_charts(df)

    print("\nPipeline completed successfully")
main()