import streamlit as st

st.title("Unit Converter")
st.write("Converter for Length, Weight, and Time")

category = st.selectbox("Select Category", ["Length", "Weight", "Time"])

# Conditional dropdown for selecting the unit based on the category
if category == "Length":
    unit = st.selectbox("Select Unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Unit", [
        "Minutes to Hours", "Hours to Minutes",
        "Seconds to Minutes", "Minutes to Seconds",
        "Hours to Days", "Days to Hours"
    ])

value = st.number_input("Enter Value", step=0.1)

# Function to perform the unit conversion
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value * 1.60934

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None  # Fallback in case of unexpected input

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Conversion failed. Please check your inputs.")







