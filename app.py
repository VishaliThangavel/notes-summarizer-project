import streamlit as st
from summarizer import summarize_text
from extractor import extract_concepts

st.title("Intelligent Digital Notes Summarizer & Concept Extractor")

text = st.text_area("Enter your notes", height=300)

if st.button("Analyze"):
    
    if text:
        
        summary = summarize_text(text)
        concepts = extract_concepts(text)
        
        st.subheader("Summary")
        st.write(summary)
        
        st.subheader("Concepts")
        for concept in concepts:
            st.write(concept)
            
    else:
        st.write("Please enter text")