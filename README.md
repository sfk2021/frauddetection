# Credit Card Fraud Detection

## 📌 Project Overview

This project is an end-to-end **Credit Card Fraud Detection system** developed using **Python, Machine Learning, FastAPI/Backend API, and Streamlit**.

The system is designed to predict whether a credit card transaction is:

* **Legitimate**
* **Fraudulent**

The project consists of two deployed components:

1. **Backend API** – deployed on Render
2. **Frontend Web Application** – deployed on Streamlit Community Cloud

This separation allows the machine-learning prediction functionality to run through a backend API while the Streamlit application provides an easy-to-use interface for the user.

---

## 🌐 Live Application

### Frontend — Streamlit

The Streamlit frontend provides the user interface for interacting with the fraud-detection system.

**Live Streamlit Application:**
[Open Credit Card Fraud Detection App](https://frauddetection-aap6esb9ycyikrjdneh8nu.streamlit.app/)

### Backend — Render

The backend provides the API functionality used by the application for fraud-detection operations.

**Live Backend API:**
[Open Backend on Render](https://frauddetection-qd3r.onrender.com/)

---

## 🏗️ System Architecture

The project follows a frontend-backend architecture:


                    USER
                      │
                      ▼
          ┌─────────────────────┐
          │ Streamlit Frontend  │
          │                     │
          │ User Interface      │
          │ Transaction Input   │
          │ Prediction Display  │
          └──────────┬──────────┘
                     │
                     │ API Request
                     ▼
          ┌─────────────────────┐
          │   Render Backend    │
          │                     │
          │ API / Prediction    │
          │ Data Processing     │
          │ ML Model            │
          └──────────┬──────────┘
                     │
                     ▼
             Fraud Prediction
                ↙       ↘
          Legitimate    Fraudulent
           Class 0       Class 1


### Deployment

| Component   | Platform                  | Purpose                                  |
| ----------- | ------------------------- | ---------------------------------------- |
| Frontend    | Streamlit Community Cloud | User interface                           |
| Backend     | Render                    | API and prediction processing            |
| Source Code | GitHub                    | Version control and project repository   |
| Dataset     | GitHub                    | Transaction data used by the application |

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze credit card transaction data.
* Identify patterns associated with fraudulent transactions.
* Develop a machine-learning classification system.
* Predict whether a transaction is legitimate or fraudulent.
* Build a backend API for prediction functionality.
* Develop an interactive Streamlit frontend.
* Deploy the backend and frontend online.
* Demonstrate an end-to-end machine-learning application.

---

## 📊 Dataset

The project uses a credit card transaction dataset containing anonymized transaction features.

The original dataset contains approximately **284,807 transactions**, including legitimate and fraudulent transactions.

For this deployed project, a smaller dataset was prepared to make the application more suitable for GitHub and Streamlit deployment.

### Dataset used

* **Total transactions:** 10,000
* **Fraudulent transactions:** 492
* **Legitimate transactions:** 9,508
* **Total columns:** 31
* **Target column:** `Class`

The `Class` column represents the transaction type:

| Class | Meaning                |
| ----- | ---------------------- |
| `0`   | Legitimate transaction |
| `1`   | Fraudulent transaction |

All fraudulent transactions from the original dataset were retained in the smaller dataset. A sample of legitimate transactions was selected to reduce the overall dataset size.

---

## 🤖 Machine Learning

Fraud detection is treated as a **binary classification problem**.

The model learns patterns from historical transaction data and predicts one of two classes:


Class 0 → Legitimate Transaction

Class 1 → Fraudulent Transaction


The dataset contains anonymized numerical features such as:

* `Time`
* `Amount`
* `V1` through `V28`
* `Class`

The anonymized `V1`–`V28` features represent transformed transaction characteristics.

---

## 🔄 Application Workflow

The general workflow is:


Transaction Data
       ↓
Data Preprocessing
       ↓
Machine Learning Model
       ↓
Backend API
       ↓
Streamlit Frontend
       ↓
Prediction
       ↓
Legitimate / Fraudulent


When a user interacts with the Streamlit application, the required transaction information is processed and sent through the application's prediction workflow.

The backend handles the prediction functionality and returns the result to the frontend.

---

## 🖥️ Frontend

The frontend is developed using **Streamlit**.

It provides a simple web interface so users can interact with the fraud-detection system without directly working with Python code or API requests.

### Frontend responsibilities

* Provide an interactive user interface.
* Accept transaction information.
* Communicate with the backend.
* Display the prediction result.
* Make the machine-learning system easy to demonstrate.

### Live Frontend

[Streamlit Fraud Detection Application](https://frauddetection-aap6esb9ycyikrjdneh8nu.streamlit.app/)

---

## ⚙️ Backend

The backend is deployed using **Render**.

It provides the server-side functionality required for the application, including communication with the machine-learning prediction workflow.

### Backend responsibilities

* Receive prediction requests.
* Process the supplied transaction data.
* Apply the required preprocessing.
* Use the machine-learning model.
* Return the prediction result to the frontend.

### Live Backend

[Render Backend API](https://frauddetection-qd3r.onrender.com/)

---



### Important Files

**`app.py`**
Contains the Streamlit frontend application.

**`data/creditcard.csv`**
Contains the smaller credit-card transaction dataset used by the project.

**`requirements.txt`**
Contains the Python dependencies required to run the application.

**`README.md`**
Contains documentation and instructions for the project.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Frontend

* Streamlit

### Backend

* Python-based API/backend

### Deployment

* GitHub
* Render
* Streamlit Community Cloud

---

## 🚀 Running the Project Locally

### 1. Clone the repository


git clone https://github.com/sfk2021/frauddetection.git


Move into the project directory:


cd frauddetection


### 2. Create a virtual environment


python -m venv venv


On Windows:


venv\Scripts\activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Run the Streamlit application


streamlit run app.py


The application will provide a local URL that can be opened in a web browser.

---

## ☁️ Deployment

### GitHub

GitHub is used for source-code management and version control.

Repository:

**`sfk2021/frauddetection`**

The repository contains the application source code, dataset, requirements, and documentation.

### Render

The backend is deployed on Render.

**Live backend:**
[Fraud Detection Backend](https://frauddetection-qd3r.onrender.com/)

### Streamlit Community Cloud

The frontend is deployed using Streamlit Community Cloud.

**Live application:**
[Fraud Detection Streamlit App](https://frauddetection-aap6esb9ycyikrjdneh8nu.streamlit.app/)

---

## 👨‍💻 Project Information

**Project:** Credit Card Fraud Detection

**GitHub Repository:**
`sfk2021/frauddetection`

**Frontend:** Streamlit Community Cloud

**Backend:** Render

**Machine Learning:** Binary Classification

**Dataset:** Credit Card Transactions

---

## ⭐ Conclusion

This project demonstrates an end-to-end machine-learning solution for **credit card fraud detection**.

The system combines:

**Data → Machine Learning → Backend API → Streamlit Frontend → Cloud Deployment**

The backend is deployed on Render, while the user-facing application is deployed on Streamlit Community Cloud. GitHub is used to manage and maintain the project source code.

The project demonstrates how a machine-learning model can be transformed from a Python-based experiment into an accessible web application that can be used for demonstration and educational purposes.



