# -*- coding: utf-8 -*-
"""testing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oawu_JypP45ysYRo5L0H-WJCifWZsqvi
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# Add a background image using custom CSS
background_image_path = "header.jpg"
st.image(background_image_path, use_column_width=True)  # Adjust 'use_column_width' based on your preference
st.title('Fraudelent Job Posting Predictor')
st.write("Our data product is a predictive analytics tool crafted to aid in identifying fake job postings. Using a Random Forest model, the system analyzes job descriptions from job listings to support informed decision-making.")

# Load data from the CSV file
data = pd.read_csv("fake_job_postings.csv")

# Extract job descriptions and labels from the data
train_data = data['description'].astype(str).tolist()  # Assuming 'description' is the column containing job descriptions
train_labels = data['fraudulent'].tolist()  # Assuming 'fraudulent' is the column containing labels (1 for fake, 0 for real)

# Define the model
rf_classifier = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', RandomForestClassifier()),
])

# Fit TF-IDF vectorizer and classifier with training data
rf_classifier.fit(train_data, train_labels)

def predict_fake_job_posting(job_description):
    # Make predictions using the loaded model
    prediction = rf_classifier.predict([job_description])
    return prediction[0]

def main():
    job_description = st.text_area('Enter job description here:')
    if st.button('Predict'):
        prediction = predict_fake_job_posting(job_description)
        if prediction == 1:
            st.write('Prediction: ', unsafe_allow_html=True)
            st.write('<span style="color:red;">Fake</span>', unsafe_allow_html=True)
        else:
            st.write('Prediction: ', unsafe_allow_html=True)
            st.write('<span style="color:green;">Real</span>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

st.write("<b>WQD7006 Machine Learning For Data Science - Group 15:</b><br>Law Jia Jin, Lim Sze Sing, Gan Jing Wen, Nur Shafiqah, Nur Nazifa</br>", unsafe_allow_html=True)

