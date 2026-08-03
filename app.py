"""
Titanic Survival Prediction - Streamlit Application
This application predicts passenger survival on the Titanic using a pre-trained ML pipeline.
"""

import streamlit as st
import pickle
import pandas as pd
import os

# ================================
# PAGE CONFIGURATION
# ================================
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="wide"
)

# ================================
# LOAD THE TRAINED MODEL
# ================================
@st.cache_resource
def load_model():
    """
    Load the pre-trained machine learning pipeline from disk.
    The pipeline includes all preprocessing steps (imputation, encoding, scaling).
    """
    model_path = "titanic_model.pkl"
    
    # Check if model file exists
    if not os.path.exists(model_path):
        st.error(f"❌ Model file '{model_path}' not found! Please ensure the file exists in the project directory.")
        st.stop()
    
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

# Load the model
model = load_model()

# ================================
# SIDEBAR - PROJECT INFORMATION
# ================================
st.sidebar.header("📊 Project Information")
st.sidebar.markdown("""
**Project Name:**  
Titanic Survival Prediction

**Model Used:**  
Machine Learning Pipeline  
(Preprocessing + Classification)

**Dataset:**  
Titanic - Machine Learning from Disaster

**Developer:**  
Shah Hassan Nawab

---
**About:**  
This application predicts whether a passenger would survive the Titanic disaster based on their characteristics.
""")

# ================================
# MAIN PAGE - TITLE AND DESCRIPTION
# ================================
st.title("🚢 Titanic Survival Prediction")
st.markdown("""
Welcome to the **Titanic Survival Prediction** application!  
Enter passenger details below to predict their likelihood of survival on the Titanic.
""")

st.markdown("---")

# ================================
# INPUT FORM - USER INPUTS
# ================================
st.subheader("🎫 Passenger Information")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Passenger Class (1 = First, 2 = Second, 3 = Third)
    pclass = st.selectbox(
        "🎟️ Passenger Class",
        options=[1, 2, 3],
        help="1 = First Class, 2 = Second Class, 3 = Third Class"
    )
    
    # Sex
    sex = st.selectbox(
        "👤 Sex",
        options=["male", "female"],
        help="Passenger's gender"
    )
    
    # Age
    age = st.number_input(
        "🎂 Age",
        min_value=0.0,
        max_value=100.0,
        value=30.0,
        step=1.0,
        help="Passenger's age in years"
    )
    
    # SibSp (Number of Siblings/Spouses aboard)
    sibsp = st.number_input(
        "👨‍👩‍👧 Number of Siblings/Spouses Aboard",
        min_value=0,
        max_value=10,
        value=0,
        step=1,
        help="Number of siblings or spouses traveling with the passenger"
    )

with col2:
    # Parch (Number of Parents/Children aboard)
    parch = st.number_input(
        "👶 Number of Parents/Children Aboard",
        min_value=0,
        max_value=10,
        value=0,
        step=1,
        help="Number of parents or children traveling with the passenger"
    )
    
    # Fare
    fare = st.number_input(
        "💰 Fare (in £)",
        min_value=0.0,
        max_value=600.0,
        value=50.0,
        step=0.1,
        help="Ticket fare paid by the passenger"
    )
    
    # Embarked (Port of Embarkation)
    embarked = st.selectbox(
        "⚓ Port of Embarkation",
        options=["S", "C", "Q"],
        help="S = Southampton, C = Cherbourg, Q = Queenstown"
    )

st.markdown("---")

# ================================
# PREDICTION BUTTON AND RESULTS
# ================================
if st.button("🔮 Predict Survival", type="primary", use_container_width=True):
    try:
        # Create DataFrame with exact column names and order expected by the pipeline
        new_data = pd.DataFrame({
            "Pclass": [pclass],
            "Sex": [sex],
            "Age": [age],
            "SibSp": [sibsp],
            "Parch": [parch],
            "Fare": [fare],
            "Embarked": [embarked]
        })
        
        # Make prediction using the loaded pipeline
        # The pipeline handles all preprocessing internally
        prediction = model.predict(new_data)[0]
        
        # Display prediction result
        st.markdown("### 📋 Prediction Result")
        
        if prediction == 1:
            st.success("✅ **Passenger is likely to SURVIVE.**")
            st.balloons()
        else:
            st.error("❌ **Passenger is unlikely to survive.**")
        
        # Optional: Show the input data summary
        with st.expander("📊 View Input Data Summary"):
            st.dataframe(new_data, use_container_width=True)
            
    except Exception as e:
        st.error(f"❌ An error occurred during prediction: {str(e)}")
        st.info("Please check that all inputs are valid and try again.")

# ================================
# FOOTER
# ================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>Built with ❤️ using Streamlit | Titanic Dataset from Kaggle</p>
    <p style='font-size: 12px;'>This is a machine learning demonstration project.</p>
</div>
""", unsafe_allow_html=True)
