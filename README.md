# Heart Attack Prediction Web Application

# Features
   - User Authentication: Secure signup and login system with MySQL database
   - Heart Attack Prediction: ML-powered risk assessment based on medical parameters
   - Interactive Dashboard: Data visualization and health metrics display
   - Responsive Design: Modern UI with heart-themed styling
   - Real-time Processing: Instant prediction results

# Technology Stack
   - Backend: Flask (Python)
   - Database: MySQL
   - Machine Learning: Scikit-learn
   - Frontend: HTML5, CSS3, JavaScript
   - Data Processing: Pandas, NumPy

#Dataset
Cleveland Heart Disease Dataset:
https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
UCI Heart Disease Dataset (combined):
https://www.kaggle.com/datasets/ronitf/heart-disease-uci

# Project Structure
heart_attack_project/
├── app.py                
├── train_model.py        
├── README.md              
├── data/                  
│   └── heart_combined_cleaned.csv
├── model/                
│   ├── heart_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
├── static/              
│   ├── heart.jpg
│   └── login_bg.png
└── templates/             
    ├── index.html
    ├── login.html
    ├── signup.html
    ├── home.html
    └── dashboard.html

# Installation
- Python 3.7
- MySQL Server
- pip (Python package manager)
   pip install flask pandas scikit-learn mysql-connector-python joblib
  
 #Database Setup
   - Create MySQL database named `heart_app`
   - Update database credentials in `app.py` (lines 23-28)
   - Create users table:
     ```sql
     CREATE TABLE users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(50) UNIQUE NOT NULL,
         email VARCHAR(100) UNIQUE NOT NULL,
         password VARCHAR(255) NOT NULL
     );

#Train the Model
   python train_model.py

#Run the Application
   python app.py

#Usage
1. Sign Up: Create a new account with username, email, and password
2. Login: Access your account using credentials
3. Prediction: Enter medical parameters to get heart attack risk assessment
4. Dashboard: View health metrics and visualization

# Data Cleaning and Preprocessing

# Dataset Overview
The application uses a combined heart disease dataset (`heart_combined_cleaned.csv`) that has been thoroughly cleaned and preprocessed for machine learning.

# Data Cleaning Steps

1. **Column Name Standardization**
   - Strip whitespace from column names
   - Ensure consistent naming conventions
   - Remove any special characters

2. **Missing Value Handling**
   - Remove rows with critical missing values
   - Impute missing values where appropriate
   - Validate data integrity

3. **Data Type Conversion**
   - Convert categorical variables to proper data types
   - Ensure numerical features are in correct format
   - Validate range constraints for medical parameters

# Preprocessing Pipeline

1. Categorical Feature Encoding
categorical_cols = ['cp', 'restecg', 'slope', 'thal', 'sex', 'fbs', 'exang']
# One-Hot Encoding with drop_first=True to avoid multicollinearity
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
2. Feature Selection
    -Removed Features: `id`, `dataset` (non-predictive identifiers)
    - Target Variable: `num` converted to binary classification
    - `num > 0` → 1 (Heart disease present)
    - `num = 0` → 0 (No heart disease)
3. Numerical Feature Scaling
numeric_cols = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']'

# StandardScaler for normalization
scaler = StandardScaler()
X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

4. Train-Test Split
     - Split Ratio: 80% training, 20% testing
     - Random State: 42 for reproducibility
     - Stratification: Maintains class distribution

# Feature Engineering Details
# Categorical Variables
- Chest Pain Type (cp): 4 types encoded as dummy variables
- Resting ECG (restecg): 3 categories encoded
- ST Slope (slope): 3 categories encoded
- Thalassemia (thal): 3 types encoded
- Sex: Binary encoding
- Fasting Blood Sugar (fbs): Binary encoding
- Exercise Angina (exang): Binary encoding

# Numerical Variables
- Age: Patient age in years
- Resting Blood Pressure (trestbps): mm Hg
- Cholesterol (chol): mg/dl
- Max Heart Rate (thalch): bpm
- ST Depression (oldpeak): Exercise-induced depression
- Major Vessels (ca): Count (0-3)

# Data Quality Assurance

1. Outlier Detection
   - Identify extreme values in numerical features
   - Apply domain-specific constraints (e.g., age ranges)
   - Handle outliers appropriately

2. Consistency Checks
   - Validate relationships between features
   - Check for logical inconsistencies
   - Ensure medical parameter ranges are realistic

3. Feature Importance Analysis
   - Evaluate feature correlations
   - Remove highly correlated features
   - Select most predictive variables

# Model Training Pipeline
python
# Complete preprocessing workflow
1. Load cleaned dataset
2. Validate column names and data types
3. Apply one-hot encoding to categorical features
4. Drop non-predictive columns
5. Convert target to binary classification
6. Split data into train/test sets
7. Scale numerical features
8. Train Random Forest model
9. Save model, scaler, and column information

# Model Details

The application uses a machine learning model trained on heart disease datasets with the following features:

- Input Features: Age, sex, chest pain type, blood pressure, cholesterol, etc.
- Algorithm: Random Forest Classifier
- Preprocessing: StandardScaler for numerical features, One-Hot Encoding for categorical features
- Output: Binary classification (0 = Low Risk, 1 = High Risk)

# Medical Parameters Used

- `age`: Patient age
- `sex`: Gender (0 = female, 1 = male)
- `cp`: Chest pain type (1-4)
- `trestbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (0 = false, 1 = true)
- `restecg`: Resting electrocardiographic results (0-2)
- `thalch`: Maximum heart rate achieved
- `exang`: Exercise induced angina (0 = no, 1 = yes)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: Slope of the peak exercise ST segment (1-3)
- `ca`: Number of major vessels colored by fluoroscopy (0-3)
- `thal`: Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)

# API Endpoints

- `GET /` - Landing page
- `GET /login` - Login page
- `POST /login` - User authentication
- `GET /signup` - Registration page
- `POST /signup` - User registration
- `GET /home` - Main application interface
- `POST /predict` - Heart attack prediction endpoint
- `GET /dashboard` - Data visualization dashboard

