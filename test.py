import google.generativeai as genai

# Set up your API key
key = 'AIzaSyB--Kl3a3a3gY-3AsntQeSjgQwUp_NnPio'  # Replace with your new API key
genai.configure(api_key=key)

# Test the API
try:
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content("Generate 10 multiple choice questions for the subject 'HTML' with options and correct answers")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")