import streamlit as st
import requests

st.set_page_config(page_title="Loan Default Predictor", page_icon="🏦", layout="centered")

st.title("🏦 Loan Default Prediction Dashboard")
st.markdown("### Predict whether a customer is likely to default on a personal loan")

with st.sidebar:
    st.header("📋 Input Customer Information")
    age = st.number_input("Age", min_value=18, max_value=100)
    experience = st.number_input("Experience", min_value=0, max_value=80)
    income = st.number_input("Annual Income (in $000s)", min_value=0)
    zip_code = st.text_input("ZIP Code")
    family = st.selectbox("Family Size", [1, 2, 3, 4])
    ccavg = st.number_input("Avg Credit Card Spending (in $000s)")
    education = st.selectbox("Education Level", [1, 2, 3], help="1: Undergrad, 2: Graduate, 3: Advanced")
    mortgage = st.number_input("Mortgage (in $000s)")
    personal_loan = st.selectbox("Previously Took Personal Loan?", [0, 1])
    securities_account = st.selectbox("Has Securities Account?", [0, 1])
    cd_account = st.selectbox("Has CD Account?", [0, 1])
    online = st.selectbox("Uses Online Banking?", [0, 1])
    creditcard = st.selectbox("Has Credit Card?", [0, 1])

input_data = {
    "Age": int(age),
    "Experience": int(experience),
    "Income": int(income),
    "ZIP Code": int(zip_code) if zip_code else 0,
    "Family": int(family),
    "CCAvg": float(ccavg),
    "Education": int(education),
    "Mortgage": float(mortgage),
    "Personal Loan": int(personal_loan),
    "Securities Account": int(securities_account),
    "CD Account": int(cd_account),
    "Online": int(online),
    "CreditCard": int(creditcard)
}

if st.button("🔍 Predict Loan Default"):
    try:
        API_URL = "http://127.0.0.1:5000/predict"
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            st.subheader("🔮 Prediction Outcome")
            st.success("✅ Will Not Default" if prediction == 0 else "⚠️ Will Default")
            
            st.markdown("---")
            st.markdown("### 📊 Prediction Details")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Credit Card Usage", f"${ccavg * 1000:.2f}")
                st.metric("Mortgage", f"${mortgage * 1000:.2f}")
            with col2:
                st.metric("Income", f"${income * 1000:.2f}")
                st.metric("Risk Level", "Low" if prediction == 0 else "High", delta="-85%" if prediction == 0 else "+70%")

            st.markdown("---")
            st.info("🔍 Insight: Customers with income above $60K and no prior loan history are less likely to default.")
        else:
            st.error("Failed to get prediction from API.")
    except Exception as e:
        st.error(f"Error: {e}")


if __name__ == "__main__":
    st.set_page_config(page_title="Loan Default Predictor", layout="wide")
    st.markdown("<style>footer{visibility: hidden;}</style>", unsafe_allow_html=True)

