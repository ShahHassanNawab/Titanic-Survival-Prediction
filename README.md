# 🚢 Titanic Survival Prediction

An end-to-end Machine Learning web application that predicts whether a passenger would survive the Titanic disaster using a trained **Scikit-learn Pipeline** and **Streamlit**.

---

## 🌐 Live Demo

🔗 https://titanic-survival-prediction-ctfqddodwixkexqtaeckpc.streamlit.app/

---

## 📖 Project Overview

This project uses the famous **Titanic dataset** to predict passenger survival based on information such as:

- Passenger Class
- Sex
- Age
- Number of Siblings/Spouses (SibSp)
- Number of Parents/Children (Parch)
- Fare
- Embarked Port

The application provides an interactive web interface where users can enter passenger information and instantly receive a survival prediction.

---

## 📈 Model Evaluation

| Metric | Score |
|---------|------:|
| Accuracy | **62%** |

The model achieved **62% accuracy** on the test dataset.

Future improvements may include:

- Better feature engineering
- Hyperparameter tuning
- Trying different machine learning algorithms
- Cross-validation for improved generalization

---

## 📸 Streamlit Application Screenshots

### 🏠 Home Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/3860a11c-0243-4e40-9024-7212bc8b0017" width="850">
</p>

### ✅ Prediction Result

<p align="center">
  <img src="https://github.com/user-attachments/assets/e216e68a-a3cf-4727-b8d0-db2e742dfb65" width="850">
</p>

---

## 🚀 Features

- Interactive Streamlit Web Application
- Real-time Survival Prediction
- Beginner-Friendly User Interface
- Scikit-learn Pipeline
- Automatic Data Preprocessing
- Missing Value Handling
- One-Hot Encoding
- Model Serialization using Pickle
- Ready for Deployment

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 🤖 Machine Learning Workflow

```text
Titanic Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Missing Value Imputation
        │
        ▼
One-Hot Encoding
        │
        ▼
ColumnTransformer
        │
        ▼
Pipeline
        │
        ▼
Model Training
        │
        ▼
Model Saved (.pkl)
        │
        ▼
Streamlit Web Application
        │
        ▼
Prediction
```

---

## 📂 Project Structure

```text
Titanic-Survival-Prediction/
│
├── app.py
├── titanic_model.pkl
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ShahHassanNawab/Titanic-Survival-Prediction.git
```

### Navigate to the project folder

```bash
cd Titanic-Survival-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Model Input Features

| Feature | Description |
|----------|-------------|
| Pclass | Passenger Class (1, 2, or 3) |
| Sex | Male or Female |
| Age | Passenger Age |
| SibSp | Number of Siblings/Spouses |
| Parch | Number of Parents/Children |
| Fare | Passenger Ticket Fare |
| Embarked | Port of Embarkation (C, Q, S) |

---

## 🎯 Prediction Output

The application predicts one of the following outcomes:

✅ Passenger is likely to survive.

or

❌ Passenger is unlikely to survive.

---

## 📚 What I Learned

Through this project, I learned:

- Data preprocessing
- Handling missing values
- Feature engineering
- One-Hot Encoding
- ColumnTransformer
- Building Machine Learning Pipelines
- Training Machine Learning models
- Model serialization using Pickle
- Streamlit application development
- Deploying Machine Learning applications

---

## 👨‍💻 Developer

**Shah Hassan Nawab**

BS Artificial Intelligence

Institute of Space Technology (IST), Islamabad

**GitHub:** https://github.com/ShahHassanNawab

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to build more Machine Learning and Artificial Intelligence projects.
