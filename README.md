# Frootify 🍅

Frootify is a smart post-harvest monitoring system designed to predict tomato spoilage risk using environmental conditions and machine learning.

## Project Overview

The current system uses a Random Forest classifier deployed on a Raspberry Pi 4 to assess spoilage risk based on:

* Temperature
* Humidity

Environmental data is collected automatically using a DHT11 sensor connected to the Raspberry Pi.

The system then provides spoilage predictions and storage recommendations through a rule engine.

---

## Current Features

* Tomato spoilage risk prediction
* Random Forest machine learning model
* Raspberry Pi 4 deployment
* Automatic DHT11 sensor integration
* Good/Bad classification
* Spoilage probability estimation
* Shelf-life recommendations based on prediction confidence
* Actionable storage suggestions

---

## System Architecture

DHT11 Sensor

↓

Raspberry Pi 4

↓

Feature Engineering

↓

Random Forest Model

↓

Rule Engine

↓

Prediction & Recommendations

---

## Inputs

* Temperature (°C)
* Humidity (%)

## Engineered Features

* Temp
* Humid (%)
* Temp_Humidity
* High_Humidity

## Outputs

* Good / Bad Prediction
* Bad Probability (%)
* Shelf Recommendation
* Suggested Actions

---

## Tech Stack

* Python
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Raspberry Pi 4
* DHT11 Sensor

---

## Project Structure

frootify/

├── src/

│   ├── app.py

│   ├── predict.py

│   ├── rule_engine.py

│   └── models/

│       ├── fruit_spoilage_rf_tomato.pkl

│       ├── feature_order_tomato.pkl

│       └── preprocessing_tomato.pkl

├── README.md

└── .gitignore

---

## Future Work

The next phase of Frootify is currently under development.

A computer vision model is being trained to classify tomatoes as:

* Fresh
* Rotten

using image classification techniques.

The long-term goal is to combine:

* Environmental risk assessment (sensor model)
* Visual spoilage detection (image model)

to create a more robust hybrid spoilage monitoring system.

---

## Running the Project

From the src directory:

python app.py

The Raspberry Pi automatically reads data from the DHT11 sensor and generates spoilage predictions and recommendations.

---

Built as a smart post-harvest tomato monitoring system combining IoT and Machine Learning.
