# -*- coding: utf-8 -*-
# coding: utf-8

import streamlit as st

# App Title
st.title("BMI Calculator")

# User Input Fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")