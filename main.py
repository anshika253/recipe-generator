import streamlit as st
from google import genai

st.set_page_config(page_title="AI Recipe Generator", page_icon="🍳")
st.title("🍳 AI Recipe Generator")
st.write("Enter a dish name OR a few ingredients you have at home, and get a full recipe!")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

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
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                st.markdown(response.text)
            except Exception as e:
                st.error(f"DEBUG ERROR: {e}")
