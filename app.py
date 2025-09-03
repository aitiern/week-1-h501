import streamlit as st

from apputil import *

from exercises import palindrome, parentheses, parentheses_alt, findLargestNumber

st.write(
    """
    # Week 1: Introduction to the Python Coding Environment
    
    Try out the functions you built for your exercises.
    """
)

# Sidebar menu
st.sidebar.header("Choose an Exercise")
exercise = st.sidebar.radio("Select:", ["Palindrome", "Parentheses", "Largest Number"])

# --- Palindrome ---
if exercise == "Palindrome":
    st.subheader("Palindrome Checker")
    text = st.text_input("Enter text:")
    if text:
        if palindrome(text):
            st.success(f"'{text}' is a palindrome")
        else:
            st.error(f"'{text}' is not a palindrome")

# --- Parentheses ---
elif exercise == "Parentheses":
    st.subheader("Balanced Parentheses")
    seq = st.text_input("Enter a string with parentheses:")
    if seq:
        st.write("**Method 1 result:**", parentheses(seq))
        st.write("**Method 2 result:**", parentheses_alt(seq))

# --- Largest Number ---
else:
    st.subheader("Find Largest Number")
    words = st.text_area("Paste text (space-separated words):", height=150)
    if words:
        word_list = words.split()
        largest = findLargestNumber(word_list)
        if largest is not None:
            st.success(f"Largest number found: {largest}")
        else:
            st.warning("No numbers found in your text.")
