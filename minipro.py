# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if status == 'cms':
    height = st.number_input('Centimeters')

    try:
        bmi = weight / ((height / 100) ** 2)
    except ZeroDivisionError:
        st.text("Enter some value of height")
elif status == 'meters':
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except ZeroDivisionError:
        st.text("Enter some value of height")

if st.button('Calculate BMI'):
    # print the BMI INDEX
    st.text("Your BMI Index is {:.2f}.".format(bmi))

    # give the interpretation of BMI index
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Extremely Overweight")
