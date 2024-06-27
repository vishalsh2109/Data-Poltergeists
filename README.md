# Prediction-Form Flask Application

This Flask application predicts whether a patient needs to be readmitted based on input data. It uses a machine learning model trained on various patient parameters.

## Features

- Predicts the need for patient readmission based on:
  - Age
  - Gender
  - Ethnicity
  - Admission type
  - Insurance type
  - Marital status
  - Length of stay (computed from admit and discharge dates)
  
## Setup Instructions

### Prerequisites

- 3.7>= Python <=3.10.12
- Pip package manager

### Installation

Clone the repository:

```bash
git clone https://github.com/vishalsh2109/Data-Poltergeists.git
cd Prediction-Form-Flask-App
```
Install dependencies:
```bash
pip install Flask numpy scikit-learn
```
Run the application:
```bash
python app.py
```
The application should now be running locally at http://localhost:5000.

Navigate to http://localhost:5000/ in your web browser to access the prediction form.

Fill in the patient details and submit the form.

The application will predict whether the patient needs to be readmitted.
