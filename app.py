import streamlit as st
import pandas as pd
import numpy as np
from database import (init_db, add_user, check_user, save_prediction,
                      get_user_predictions)
from models.health_predictor import (HealthFactorsPredictor, DemographicPredictor,
                                     SocioeconomicPredictor, LifestylePredictor)
from utils.model_manager import ModelManager
from utils.visualizations import render_history_tab


def render_predictor_ui(predictor, prediction_type):
    st.subheader(f"{prediction_type} Analysis")

    # Train the model
    accuracy = predictor.train()
    # if accuracy:
    #     st.write(f"Model Accuracy: {accuracy:.2f}")

    # Create input form
    st.write("Enter your information:")
    user_input = {}
    for feature in predictor.features:
        if feature == 'BMI':
            user_input[feature] = st.number_input(
                f"Enter your {feature}", 15.0, 60.0, 25.0)
        elif feature in ['Age', 'Education', 'Income']:
            user_input[feature] = st.slider(f"Select your {feature}", 1, 13, 6)
        else:
            user_input[feature] = st.selectbox(f"{feature}", [0, 1])

    if st.button("Predict"):
        input_df = pd.DataFrame([user_input])
        prediction, probabilities = predictor.predict(input_df)

        risk_level = ["No Diabetes", "Pre-diabetes",
                      "Diabetes"][int(prediction[0])]
        st.write(f"Predicted Risk Level: {risk_level}")
        st.write(f"Prediction Probability: {max(probabilities[0])*100:.2f}%")

        # Save prediction
        if 'username' in st.session_state:
            save_prediction(
                st.session_state.username,
                prediction_type,
                risk_level,
                float(max(probabilities[0])),
                str(user_input),
                str(predictor.features),
                float(accuracy)
            )

        # Show visualizations
        predictor.plot_all_visualizations()


def main():
    st.title("Diabetes Risk Prediction System")

    # Initialize database
    init_db()

    # Session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Login/Signup sidebar
    with st.sidebar:
        if not st.session_state.logged_in:
            st.subheader("Login/Signup")
            login_tab, signup_tab = st.tabs(["Login", "Signup"])

            with login_tab:
                login_user = st.text_input("Username", key="login_user")
                login_pass = st.text_input(
                    "Password", type='password', key="login_pass")
                if st.button("Login"):
                    if check_user(login_user, login_pass):
                        st.session_state.logged_in = True
                        st.session_state.username = login_user
                        st.rerun()
                    else:
                        st.error("Invalid credentials")

            with signup_tab:
                new_user = st.text_input("Username", key="new_user")
                new_pass = st.text_input(
                    "Password", type='password', key="new_pass")
                new_name = st.text_input("Full Name", key="new_name")
                if st.button("Sign Up"):
                    if add_user(new_user, new_pass, new_name):
                        st.success("Account created! Please login.")
                    else:
                        st.error("Username already exists")
        else:
            st.write(f"Welcome, {st.session_state.username}!")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()

    # Main content
    if st.session_state.logged_in:
        # Create tabs for prediction and history
        tab1, tab2 = st.tabs(["Make Prediction", "History"])

        with tab1:
            analysis_type = st.selectbox(
                "Select Analysis Type",
                ["Health Factors Analysis",
                 "Demographic Factors Analysis",
                 "Socioeconomic Analysis",
                 "Lifestyle Habits Analysis"]
            )

            if analysis_type == "Health Factors Analysis":
                predictor = HealthFactorsPredictor()
            elif analysis_type == "Demographic Factors Analysis":
                predictor = DemographicPredictor()
            elif analysis_type == "Socioeconomic Analysis":
                predictor = SocioeconomicPredictor()
            else:
                predictor = LifestylePredictor()

            render_predictor_ui(predictor, analysis_type)

        with tab2:
            render_history_tab(st.session_state.username)


if __name__ == "__main__":
    main()
