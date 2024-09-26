# # Summary
# # Pros Analysis
# # Cons Analysis
# # Red Flags Detection
# # Cultural Fit and Soft Skills Insights
# # Long-Term potential
# # Q&A Chatbot follow up questions 

import streamlit as st
import PyPDF2
import time
import pdfplumber
import json
import uuid
from setup import *
import random
import requests

def retrieve_job_matching(session_id):
    api = "http://127.0.0.1:8000/post-retrieve-all-outputs?session_id=<<id>>"
    response = requests.get(api.replace("<<id>>",session_id))
    return response.json()

matching_retriever = None
uploaded_file = None
first_time = True
# Title of the app
st.title("Generative AI-based CV Analysis")
session_id = str(uuid.uuid1())
""" UPLOADING CV FILE """

# File uploader
if first_time:
    uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
    # Check if a file is uploaded
    if (uploaded_file is not None):
        # If it's a PDF file
        if uploaded_file.type == "application/pdf":
            # Extract text from PDF
            with pdfplumber.open(uploaded_file) as pdf:
                pdf_text = ''
                for page in pdf.pages:
                    pdf_text += page.extract_text()
                print(pdf_text)
                collection_cvinput.insert_one({"session_id":session_id,"content":pdf_text})
                print("successful upload to database")
                first_time = False

if (uploaded_file is not None):
    matching_retriever = retrieve_job_matching(session_id)
    # Define sticker-like icons for pros, cons, and red flags (you can replace with your preferred icons or emojis)
    pros_icon = "✅"
    cons_icon = "❌"
    red_flag_icon = "🚩" 
    cultural_fit_icon = "🤝"
    long_term_icon = "🎯" 

    for i in range(1,6):
        # Title of the app
        st.title(f"Job Matching #{i} - {matching_retriever[f"job_matching_{i}"]["role"]}")
        # Section for Pros and Cons
        st.header("Pros and Cons")
        pros_list_i = [j for j in matching_retriever[f"job_matching_{i}"]["pros_analysis"].values() if j.lstrip().rstrip()!='None']
        cons_list_i = [j for j in matching_retriever[f"job_matching_{i}"]["cons_analysis"].values() if j.lstrip().rstrip()!='None']
        # Display Pros
        st.subheader("Pros")
        for pro in pros_list_i:
            st.markdown(f"{pros_icon} {pro}")
        # Display Cons
        st.subheader("Cons")
        for con in cons_list_i:
            st.markdown(f"{cons_icon} {con}")
        # Section for Red Flags
        st.header(f"Red Flags Indication {red_flag_icon}")
        # Display Red Flags
        st.markdown(f"{matching_retriever[f"job_matching_{i}"]["red_flags_indication"]}")

        # Section for Cultural Fit and Soft Skills Insights
        st.header(f"Cultural Fit and Soft Skills Insights {cultural_fit_icon}")
        # Display Cultural Fit and Soft Skills Insights
        st.markdown(f"{matching_retriever[f"job_matching_{i}"]["cultural_fit_and_soft_skills_insights"]}")

        # Section for Long-Term Potential
        st.header(f"Long-Term Potential {long_term_icon}")
        # Display Cultural Fit and Soft Skills Insights
        st.markdown(f"{matching_retriever[f"job_matching_{i}"]["long_term_potential"]}")
