# Academic Guide AI

An AI-powered academic guidance system that provides students with an initial recommendation of suitable colleges based on their personality traits and interests.

## Project Overview

Academic Guide AI is a machine learning-based system designed to help students who may feel uncertain when choosing a suitable college.
The system analyzes the student's responses to a set of questions derived from psychological and personality-related concepts. A trained Random Forest model then analyzes these responses and generates an initial recommendation of the most suitable colleges for the student.
The system is designed to provide an initial perspective and does not replace professional academic counseling.

## Problem

Many students experience uncertainty when choosing a suitable college and may struggle to identify which educational environment could be a good fit for their interests and personality.
Students may ask questions such as:

Which college may be suitable for me?
Does my personality fit this college?
Which college could match my interests?

Academic Guide AI aims to provide students with an initial, data-driven perspective to help them explore their options.

## Solution

The system collects the student's responses through a set of questions derived from psychological and personality-related concepts.
The responses are processed and passed to a trained Random Forest machine learning model. The model generates predictions for the available colleges, and the system presents the top recommended colleges to the student.
## Technologies Used

## Machine Learning & Data Processing

Python
Scikit-learn
Random Forest Classifier
Pandas
NumPy

## Backend

Flask
Database
SQLite

## Frontend
HTML
CSS
JavaScript

## How It Works

The student answers a set of personality and interest-related questions.
The responses are collected and processed.
Pandas and NumPy are used for data processing and numerical operations.
The processed data is passed to the trained Random Forest model.
The model predicts the suitability of the available colleges.
The system ranks the predictions and displays the top recommended colleges.

## System Components
Data processing and preparation
Machine learning model
Flask backend
SQLite database
Web interface
College recommendation system

## Disclaimer
The recommendations provided by Academic Guide AI are intended as an initial guidance tool. They should not be considered a definitive academic or career decision or a substitute for professional academic counseling.
