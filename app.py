import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate MCQs
def generate_mcq(subject, number, level):
    difficulty_mapping = {
        "Bronze": "basic",
        "Silver": "intermediate",
        "Gold": "advanced",
        "Platinum": "expert",
        "Diamond": "most difficult"
    }
    difficulty = difficulty_mapping.get(level, "basic")
    prompt = f"Generate {number} multiple choice questions for the subject '{subject}' at a {difficulty} level with options and correct answers."
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)
    return response.text

# Function to generate True/False questions with marked answers
def generate_true_false(subject, number, level):
    difficulty_mapping = {
        "Bronze": "basic",
        "Silver": "intermediate",
        "Gold": "advanced",
        "Platinum": "expert",
        "Diamond": "most difficult"
    }
    difficulty = difficulty_mapping.get(level, "basic")
    prompt = f"Generate {number} True/False questions for the subject '{subject}' at a {difficulty} level, and indicate the correct answer (True or False) for each question."
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)
    return response.text

# Function to generate multiple correct answer questions
def generate_multiple_correct(subject, number, level):
    difficulty_mapping = {
        "Bronze": "basic",
        "Silver": "intermediate",
        "Gold": "advanced",
        "Platinum": "expert",
        "Diamond": "most difficult"
    }
    difficulty = difficulty_mapping.get(level, "basic")
    prompt = f"Generate {number} multiple choice questions with multiple correct answers for the subject '{subject}' at a {difficulty} level."
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)
    return response.text

# Streamlit UI
st.title("Questions Generator")

subject = st.text_input("Enter the subject:")
# User inputs in the same line
col1, col2 = st.columns(2)
with col1:
    # Dropdown for difficulty levels
    level = st.selectbox("Select difficulty level:", ["Bronze", "Silver", "Gold", "Platinum", "Diamond"])

with col2:
    number = st.number_input("Number of questions:", min_value=1, max_value=100, value=10)

# Initialize a flag to control the visibility of the export button
export_button_visible = False

# Button to generate mixed questions
if st.button("Generate Questions"):
    if subject:
        # Calculate the number of each type of question
        num_mcqs = number * 4 // 10  # 40% MCQs
        num_true_false = number * 3 // 10  # 30% True/False
        num_multiple_correct = number - (num_mcqs + num_true_false)  # Remaining for multiple correct answers

        # Generate questions
        mcq_questions = generate_mcq(subject, num_mcqs, level)
        true_false_questions = generate_true_false(subject, num_true_false, level)
        multiple_correct_questions = generate_multiple_correct(subject, num_multiple_correct, level)

        # Combine all questions into a single output
        all_questions = f"{mcq_questions}\n\n{true_false_questions}\n\n{multiple_correct_questions}"
        
        # Display all questions
        st.write("### Generated Questions:")
        st.write(all_questions)

        # Set the flag to show the export button
        export_button_visible = True
    else:
        st.error("Please enter a subject.")

# Show the export button if the questions have been generated
if export_button_visible:
    if st.button("Export to Database"):
        st.write("Export functionality is not implemented yet.")