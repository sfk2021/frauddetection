
import streamlit as st
import requests
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bank Fraud Detection",
    page_icon="💳",
    layout="wide"
)


# ============================================================
# FASTAPI BACKEND URL
# ============================================================

API_URL = "https://frauddetection-qd3r.onrender.com"


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():

    # Find project root
    project_root = Path(__file__).resolve().parent.parent

    dataset_path = project_root / "data" / "creditcard.csv"

    return pd.read_csv(dataset_path)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777777;
        font-size: 18px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">💳 Bank Transaction Fraud Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning powered fraud detection using FastAPI + Streamlit'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🔍 Fraud Detection",
        "📊 About the Model"
    ]
)


# ============================================================
# FRAUD DETECTION PAGE
# ============================================================

if page == "🔍 Fraud Detection":

    st.header("🔍 Check a Transaction")

    st.write(
        "Select a real transaction from the Credit Card Fraud Detection "
        "dataset and send it to the machine learning model."
    )

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------

    try:

        df = load_dataset()

    except FileNotFoundError:

        st.error(
            "❌ Dataset not found."
        )

        st.info(
            "Please make sure creditcard.csv is located inside "
            "the data folder."
        )

        st.stop()

    except Exception as e:

        st.error(
            "❌ Could not load the dataset."
        )

        st.exception(e)

        st.stop()


    # --------------------------------------------------------
    # DATASET INFORMATION
    # --------------------------------------------------------

    total_transactions = len(df)

    total_fraud = int(df["Class"].sum())

    total_legitimate = total_transactions - total_fraud

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Transactions",
            f"{total_transactions:,}"
        )

    with col2:
        st.metric(
            "Legitimate",
            f"{total_legitimate:,}"
        )

    with col3:
        st.metric(
            "Fraud Cases",
            f"{total_fraud:,}"
        )


    st.divider()


    # --------------------------------------------------------
    # TRANSACTION SELECTION
    # --------------------------------------------------------

    st.subheader("Select Transaction Type")

    transaction_type = st.radio(
        "Choose a transaction to test:",
        [
            "✅ Legitimate Transaction",
            "🚨 Fraudulent Transaction"
        ],
        horizontal=True
    )


    # --------------------------------------------------------
    # GET TRANSACTIONS OF SELECTED TYPE
    # --------------------------------------------------------

    if transaction_type == "✅ Legitimate Transaction":

        available_transactions = df[df["Class"] == 0]

        st.success(
            "You are testing a known legitimate transaction."
        )

    else:

        available_transactions = df[df["Class"] == 1]

        st.warning(
            "You are testing a known fraudulent transaction."
        )


    # --------------------------------------------------------
    # SELECT TRANSACTION
    # --------------------------------------------------------

    selected_index = st.selectbox(
        "Select transaction",
        available_transactions.index,
        format_func=lambda x: f"Transaction #{x}"
    )


    selected_transaction = (
        df.loc[selected_index]
        .drop("Class")
    )


    # --------------------------------------------------------
    # SHOW TRANSACTION INFORMATION
    # --------------------------------------------------------

    st.subheader("Transaction Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Transaction Time",
            f"{selected_transaction['Time']:.2f}"
        )

    with col2:

        st.metric(
            "Transaction Amount",
            f"${selected_transaction['Amount']:.2f}"
        )


    # --------------------------------------------------------
    # SHOW ORIGINAL CLASS
    # --------------------------------------------------------

    with st.expander("View Dataset Transaction Details"):

        st.write(
            "This transaction comes directly from the Kaggle "
            "Credit Card Fraud Detection dataset."
        )

        details = pd.DataFrame(
            {
                "Feature": selected_transaction.index,
                "Value": selected_transaction.values
            }
        )

        st.dataframe(
            details,
            width="stretch",
            hide_index=True
        )


    # --------------------------------------------------------
    # CHECK TRANSACTION
    # --------------------------------------------------------

    st.divider()

    check_button = st.button(
        "🔍 Check Transaction",
        type="primary",
        width="stretch"
    )


    if check_button:

        # ----------------------------------------------------
        # CREATE API REQUEST
        # ----------------------------------------------------

        transaction_data = {
            feature: float(selected_transaction[feature])
            for feature in selected_transaction.index
        }


        # ----------------------------------------------------
        # CALL FASTAPI
        # ----------------------------------------------------

        with st.spinner("Analyzing transaction..."):

            try:

                response = requests.post(
                    f"{API_URL}/predict",
                    json=transaction_data,
                    timeout=60
                )

                response.raise_for_status()

                result = response.json()

                prediction = int(result["prediction"])

                fraud_probability = float(
                    result["fraud_probability"]
                )


                # ------------------------------------------------
                # DISPLAY RESULT
                # ------------------------------------------------

                st.subheader("Prediction Result")

                probability_percentage = (
                    fraud_probability * 100
                )


                if prediction == 1:

                    st.error(
                        "🚨 FRAUDULENT TRANSACTION"
                    )

                    st.write(
                        "The model has classified this transaction "
                        "as potentially fraudulent."
                    )

                else:

                    st.success(
                        "✅ LEGITIMATE TRANSACTION"
                    )

                    st.write(
                        "The model has classified this transaction "
                        "as likely legitimate."
                    )


                # ------------------------------------------------
                # FRAUD PROBABILITY
                # ------------------------------------------------

                st.subheader("Fraud Probability")

                st.metric(
                    "Estimated Fraud Probability",
                    f"{probability_percentage:.2f}%"
                )

                st.progress(
                    min(
                        max(fraud_probability, 0.0),
                        1.0
                    )
                )


                # ------------------------------------------------
                # COMPARE WITH ACTUAL DATASET LABEL
                # ------------------------------------------------

                actual_class = int(
                    df.loc[selected_index, "Class"]
                )

                st.subheader("Model vs Actual Result")

                comparison_col1, comparison_col2 = st.columns(2)

                with comparison_col1:

                    if actual_class == 1:

                        st.write(
                            "Actual Dataset Label:"
                        )

                        st.error(
                            "🚨 Fraud"
                        )

                    else:

                        st.write(
                            "Actual Dataset Label:"
                        )

                        st.success(
                            "✅ Legitimate"
                        )


                with comparison_col2:

                    st.write(
                        "Model Prediction:"
                    )

                    if prediction == 1:

                        st.error(
                            "🚨 Fraud"
                        )

                    else:

                        st.success(
                            "✅ Legitimate"
                        )


                # ------------------------------------------------
                # CHECK WHETHER PREDICTION IS CORRECT
                # ------------------------------------------------

                if prediction == actual_class:

                    st.success(
                        "✅ The model prediction matches the "
                        "actual dataset label."
                    )

                else:

                    st.warning(
                        "⚠️ The model prediction does not match "
                        "the actual dataset label. This is possible "
                        "because machine learning models can make "
                        "incorrect predictions."
                    )


                # ------------------------------------------------
                # TECHNICAL RESULT
                # ------------------------------------------------

                with st.expander("View Technical Result"):

                    st.write(
                        "Model prediction:",
                        prediction
                    )

                    st.write(
                        "Actual class:",
                        actual_class
                    )

                    st.write(
                        "Fraud probability:",
                        f"{fraud_probability:.6f}"
                    )


            # ----------------------------------------------------
            # ERROR HANDLING
            # ----------------------------------------------------

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the FastAPI backend."
                )

                st.info(
                    "Make sure FastAPI is running with:"
                )

                st.code(
                    "uvicorn backend.main:app --reload"
                )


            except requests.exceptions.Timeout:

                st.error(
                    "❌ The request took too long. "
                    "Please try again."
                )


            except requests.exceptions.HTTPError:

                st.error(
                    f"❌ FastAPI returned an error: "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )


            except Exception as e:

                st.error(
                    "❌ Something went wrong."
                )

                st.exception(e)


# ============================================================
# MODEL INFORMATION PAGE
# ============================================================

elif page == "📊 About the Model":

    st.header("📊 About the Fraud Detection Model")

    st.write(
        """
        This application uses a Random Forest classification model
        trained on the Kaggle Credit Card Fraud Detection dataset.
        """
    )


    # --------------------------------------------------------
    # DATASET
    # --------------------------------------------------------

    st.subheader("Dataset")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Transactions",
            "284,807"
        )

    with col2:

        st.metric(
            "Fraud Cases",
            "492"
        )

    with col3:

        st.metric(
            "Input Features",
            "30"
        )


    st.info(
        """
        The dataset is highly imbalanced. Fraud represents only a very
        small percentage of all transactions, so accuracy alone is not
        a sufficient measure of model performance.
        """
    )


    # --------------------------------------------------------
    # MODEL
    # --------------------------------------------------------

    st.subheader("Machine Learning Model")

    st.write(
        """
        The project uses a Random Forest Classifier with class balancing.
        Random Forest does not require feature scaling.
        """
    )

    st.code(
        """
RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)
        """,
        language="python"
    )


    # --------------------------------------------------------
    # MODEL PERFORMANCE
    # --------------------------------------------------------

    st.subheader("Model Performance")

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:

        st.metric(
            "Fraud Precision",
            "96%"
        )

    with metric_col2:

        st.metric(
            "Fraud Recall",
            "74%"
        )

    with metric_col3:

        st.metric(
            "Fraud F1 Score",
            "84%"
        )


    st.write(
        """
        These metrics are calculated on the test dataset. Fraud recall
        indicates that the model successfully detected approximately
        74% of the fraudulent transactions in the test set.
        """
    )


    # --------------------------------------------------------
    # IMPORTANT METRICS
    # --------------------------------------------------------

    st.subheader("Important Evaluation Metrics")

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:

        st.markdown(
            """
            **Precision**

            Of the transactions predicted as fraud, how many
            were actually fraudulent?
            """
        )

        st.markdown(
            """
            **Recall**

            Of all actual fraudulent transactions, how many
            did the model successfully detect?
            """
        )


    with metric_col2:

        st.markdown(
            """
            **F1 Score**

            A balance between precision and recall.
            """
        )

        st.markdown(
            """
            **ROC-AUC**

            Measures how well the model separates fraudulent
            transactions from legitimate transactions.
            """
        )


    # --------------------------------------------------------
    # PROJECT ARCHITECTURE
    # --------------------------------------------------------

    st.subheader("Application Architecture")

    st.code(
        """
User
  │
  ▼
Streamlit UI
  │
  │ HTTP POST /predict
  ▼
FastAPI Backend
  │
  ▼
Random Forest Model
  │
  ▼
Fraud Probability
  │
  ▼
Streamlit Result
        """,
        language="text"
    )


    st.success(
        "This project demonstrates Python, Machine Learning, "
        "Random Forest, FastAPI REST APIs, Streamlit and "
        "cloud deployment."
    )




