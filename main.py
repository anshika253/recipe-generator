import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍳")
st.title("🍳 AI Recipe Generator")
st.write("Enter a dish name OR a few ingredients you have at home, and get a full recipe!")

# Configure Gemini using the secret key (we'll set this up in Streamlit Cloud)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# User input
user_input = st.text_input("Dish name or ingredients:", placeholder="e.g. Paneer Butter Masala OR rice, tomato, onion")

if st.button("Generate Recipe"):
    if user_input.strip() == "":
        st.warning("Please enter a dish name or some ingredients first.")
    else:
        with st.spinner("Cooking up your recipe..."):
            prompt = f"""
            You are a professional chef writing for complete beginners.
            The user gave this input: "{user_input}"

            If it looks like a dish name, give a full recipe for that dish.
            If it looks like a list of ingredients, suggest ONE simple dish using mainly those ingredients.

            Format your response in clean Markdown with these sections:
            ## Dish Name
            ## Ingredients (with exact measurements)
            ## Step-by-Step Instructions (numbered, with approximate time for each step)
            ## Total Time
            ## Beginner Tips
            """
            response = model.generate_content(prompt)
            st.markdown(response.text)
