import streamlit as st
from transformers import pipeline

st.title("🧠 GenAI Resume Builder")

st.write("Enter your details and generate a professional resume instantly!")

# Load AI model
generator = pipeline("text-generation", model="gpt2")

name = st.text_input("Full Name")
education = st.text_area("Education")
skills = st.text_area("Skills")
projects = st.text_area("Projects")
experience = st.text_area("Experience")

if st.button("Generate Resume"):

    prompt = f"""
    Create a professional resume for:

    Name: {name}
    Education: {education}
    Skills: {skills}
    Projects: {projects}
    Experience: {experience}

    Format it properly with headings.
    """

    result = generator(prompt, max_new_tokens=150, num_return_sequences=1)
    resume = result[0]['generated_text']

    st.subheader("Generated Resume")
    st.write(resume)
