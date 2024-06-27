from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle , datetime
app = Flask(_name_)

with open('model (6).pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('new_page'))
@app.route('/new')
def new_page():
    return render_template('new.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = request.form['gender']
    ethnicity = request.form['ethnicity']
    admission_type = request.form['admission_type']
    insurance = request.form['insurance']
    marital_status = request.form['marital_status']
    admit_date = request.form['adate']
    discharge_date = request.form['ddate']

    admit_date = datetime.datetime.strptime(admit_date, '%Y-%m-%d')
    discharge_date = datetime.datetime.strptime(discharge_date, '%Y-%m-%d')
    length_of_stay = (discharge_date - admit_date).days

    gender_dict = {'male': [0,1], 'female': [1,0]}
    ethnicity_dict = {
        'asian': [1,0,0,0,0,0], 'others': [0,0,0,0,1,0], 'black_african_american': [0,1,0,0,0,0],
        'hispanic_latino': [0,0,1,0,0,0], 'white': [0,0,0,0,0,1],  'middle_eastern': [0,0,0,1,0,0]
    }
    admission_type_dict = {'emergency': [0,1,0], 'newborn': [0,0,1], 'elective': [1,0,0]}
    insurance_dict = {
        'private': [0,0,0,1,0], 'medicaid': [0,1,0,0,0], 'medicare': [0,0,1,0,0],
        'self_pay': [0,0,0,0,1], 'government': [1,0,0,0,0]
    }
    marital_status_dict = {
        'divorced': [1,0,0,0,0,0,0], 'life_partner': [0,1,0,0,0,0,0], 'married': [0,0,1,0,0,0,0],
        'separated': [0,0,0,1,0,0,0], 'single': [0,0,0,0,1,0,0], 'widowed': [0,0,0,0,0,1,0], 'unknown': [0,0,0,0,0,0,1]
    }
    x=[length_of_stay,age]
    x.extend(gender_dict[gender])
    x.extend(ethnicity_dict[ethnicity])
    x.extend(admission_type_dict[admission_type])
    x.extend(insurance_dict[insurance])
    x.extend(marital_status_dict[marital_status])

    input_data = np.array([x]).reshape(1, -1)

    prediction = model.predict(input_data)
    if(prediction[0]==0):
        return f'No need to re-admit the patient'
    else:
        return f'Patient needs to be re-admitted'

if _name_ == '_main_':
    app.run(debug=True)