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

st.markdown("# WOD7006 MACHINE LEARNING FOR DATA SCIENCE - Group 15")

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
    st.title('Fraudelent Job Posting Predictor')
    st.write("MEMBERS: LAW JIA JIN, LIM SZE SING, GAN JING WEN, NUR SHAFIQAH, NUR NAZIFA")
    st.write("Our data product is a predictive analytics tool designed to assist the identification of fake job postings. Leveraging a Random Forest model, the system analyzes the job description posted from job listings for the informed decisions.")

    job_description = st.text_area('Enter job description here:')
    if st.button('Predict'):
        prediction = predict_fake_job_posting(job_description)
        if prediction == 1:
            st.write('Prediction: Fake')
        else:
            st.write('Prediction: Real')

if __name__ == '__main__':
    main()

