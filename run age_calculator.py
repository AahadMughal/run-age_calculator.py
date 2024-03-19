import streamlit as st
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    st.title("Age Calculator")
    
    birth_date = st.date_input("Enter your date of birth:")
    
    if st.button("Calculate Age"):
        if birth_date:
            age = calculate_age(birth_date)
            st.success(f"You are {age} years old.")
        else:
            st.error("Please enter your date of birth.")

if __name__ == "__main__":
    main()
