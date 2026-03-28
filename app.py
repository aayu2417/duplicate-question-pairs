import streamlit as st
import helper
import pickle
import os
import time

# --- Setup & Styling ---
st.set_page_config(page_title="Duplicate Question Detector", page_icon="🔍", layout="centered")

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    .confidence-text { font-size: 24px; font-weight: bold; color: #1f77b4; }
    </style>
    """, unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))

# --- UI Layout ---
st.title('🔍 Duplicate Question Detector')
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    q1 = st.text_area('Question 1', placeholder='e.g., How can I learn Python?', height=100)
with col2:
    q2 = st.text_area('Question 2', placeholder='e.g., What is the best way to learn Python?', height=100)

if st.button('Analyze Similarity'):
    if q1.strip() and q2.strip():
        with st.spinner('Predicting...'):
            # 1. Feature Engineering
            query = helper.query_point_creator(q1, q2)
            
            # 2. Get Probability (Confidence)
            # predict_proba returns [[prob_of_0, prob_of_1]]
            probability = model.predict_proba(query)[0]
            is_duplicate = probability[1] > 0.5
            confidence = probability[1] if is_duplicate else probability[0]
            
            time.sleep(0.5) # Slight delay for "feel"
            
            st.markdown("### Analysis Result")
            
            # 3. Visual Feedback based on result
            if is_duplicate:
                st.error('🔥 **These questions are likely Duplicates!**')
                # Progress bar for Duplicate probability
                st.progress(probability[1])
                st.write(f"Confidence Level: **{probability[1]*100:.2f}%**")
            else:
                st.success('✅ **These questions are Unique!**')
                # Progress bar for Unique probability
                st.progress(probability[0])
                st.write(f"Confidence Level: **{probability[0]*100:.2f}%**")

            # Warning for "Low Confidence" results
            if 0.5 < confidence < 0.65:
                st.warning("⚠️ The model is uncertain. Review manually before merging.")
                
    else:
        st.warning('⚠️ Please enter both questions before predicting.')