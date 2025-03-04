import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6d5e6;
    }
    .stHeader {
        color: #4a90e2;
        font-size: 72px; /* Increased font size */
        font-weight: bold;
        font-style: italic; /* Added italic style */
        text-align: center;
        margin-bottom: 30px; /* Added margin for spacing */
    }
    .stSelectbox, .stNumberInput, .stButton {
        margin: 10px 0;
    }
    .stButton button {
        background-color: rgb(183, 103, 167);;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #357abd;
    }
    .stSuccess {
        color: #28a745;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        background-color: #d4edda;
    }
    .stSidebar {
        background-color:rgb(183, 103, 167);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.header('🌈Welcome to the Unit Converter app')

# Sidebar for unit selection
with st.sidebar:
    st.title("Select Unit Type")
    unit_type = st.selectbox("", ["Length", "Weight", "Temperature"])

# Function to convert length
def convert_length(value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Feet":
        return value * 3.28084
    elif from_unit == "Feet" and to_unit == "Meters":
        return value / 3.28084
    elif from_unit == "Meters" and to_unit == "Inches":
        return value * 39.3701
    elif from_unit == "Inches" and to_unit == "Meters":
        return value / 39.3701
    else:
        return value

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    if from_unit == "Kilograms" and to_unit == "Pounds":
        return value * 2.20462
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return value / 2.20462
    elif from_unit == "Kilograms" and to_unit == "Ounces":
        return value * 35.274
    elif from_unit == "Ounces" and to_unit == "Kilograms":
        return value / 35.274
    else:
        return value

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        return value

# Main conversion logic
if unit_type == "Length":
    st.markdown("### Length Converter")
    length_units = ["Meters", "Feet", "Inches"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", length_units)
    with col2:
        to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter the value to convert", min_value=0.0)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.markdown(f'<p class="stSuccess">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif unit_type == "Weight":
    st.markdown("### Weight Converter")
    weight_units = ["Kilograms", "Pounds", "Ounces"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", weight_units)
    with col2:
        to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter the value to convert", min_value=0.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.markdown(f'<p class="stSuccess">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif unit_type == "Temperature":
    st.markdown("### Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", temp_units)
    with col2:
        to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter the value to convert")
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.markdown(f'<p class="stSuccess">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)