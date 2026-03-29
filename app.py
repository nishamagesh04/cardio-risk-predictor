import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

model = joblib.load('model/heart_model.pkl')
scaler = joblib.load('model/scaler.pkl')
columns = joblib.load('model/columns.pkl')

df = pd.read_csv('data/heart_combined_cleaned.csv')

app = Flask(__name__)
app.secret_key = "your_secret_key"

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nisha@04",
    database="heart_app"
)
cursor = conn.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            return redirect(url_for('login'))
        except:
            return "Username or Email already exists!"

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

        if user:
            session['user'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials!"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    total = len(df)
    male = len(df[df['sex'] == 'Male'])
    female = len(df[df['sex'] == 'Female'])
    risk = len(df[df['num'] > 0])

    return render_template(
        'dashboard.html',
        total=total,
        male=male,
        female=female,
        risk=risk
    )

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    prediction = None

    if request.method == 'POST':
        age = float(request.form['age'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        thalch = float(request.form['thalch'])
        oldpeak = float(request.form['oldpeak'])
        ca = float(request.form['ca'])

        sex = 1 if request.form['sex'] == 'Male' else 0
        fbs = 1 if request.form['fbs'] == 'True' else 0
        exang = 1 if request.form['exang'] == 'True' else 0

        cp = request.form['cp']
        restecg = request.form['restecg']
        slope = request.form['slope']
        thal = request.form['thal']

        input_dict = {
            'age': [age],
            'trestbps': [trestbps],
            'chol': [chol],
            'thalch': [thalch],
            'oldpeak': [oldpeak],
            'ca': [ca],
            'sex': [sex],
            'fbs': [fbs],
            'exang': [exang]
        }

        for col in columns:
            if col not in input_dict:
                input_dict[col] = [0]

        input_dict[f'cp_{cp}'] = [1]
        input_dict[f'restecg_{restecg}'] = [1]
        input_dict[f'slope_{slope}'] = [1]
        input_dict[f'thal_{thal}'] = [1]

        X = pd.DataFrame(input_dict)
        X = X.reindex(columns=columns, fill_value=0)

        numeric_cols = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']
        X[numeric_cols] = scaler.transform(X[numeric_cols])

        pred = model.predict(X)[0]
        prediction = "Heart Attack Risk" if pred > 0 else "No Heart Attack Risk"

    return render_template('home.html', prediction=prediction)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)