-Diabetes Prediction Using Machine Learning-

-Project Objective-
This project builds a machine learning model to predict whether a person is likely to be diabetic based on health-related features. It uses the Pima Indians Diabetes Dataset and demonstrates the end-to-end ML pipeline including training, evaluation, and web deployment using Flask.

-Tech Stack-
- Python
- scikit-learn (Logistic Regression, SVM, etc.)
- Pandas, NumPy (Data manipulation)
- Matplotlib / Seaborn (Data visualization)
- Flask (for deploying web interface)
- Jupyter Notebook

-Dataset – Pima Indians Diabetes Dataset-
- Source: UCI Machine Learning Repository
- Records: 768 samples
- Features:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- Target: `1` → Diabetic, `0` → Non-diabetic

-ML Pipeline-
1. Data Cleaning & Exploration
2. Feature Scaling
3. Model Building (Logistic Regression, SVM)
4. Model Evaluation
5. Web Deployment using Flask

-Web App-

A lightweight Flask app allows users to input values for 8 health metrics and receive a real-time diabetes prediction.

```bash
# Run the Flask app
python app.py
```

- Input: Health metrics (via form)
- Output: "You are likely diabetic" / "You are not diabetic"

---

-Results-

| Model                  | Accuracy |
|------------------------|----------|
| Logistic Regression    | ~77%     |
| Support Vector Machine | ~78%     |

> Model is saved and reused via `pickle` for fast deployment.

-How to Use-
1. Clone this repo:
   ```bash
   git clone https://github.com/sreedivyanagalli/Diabetes-Prediction.git
   cd Diabetes-Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
   
-Skills-
`Machine Learning`, `Logistic Regression`, `SVM`, `Flask`, `Model Deployment`, `Python`, `Healthcare Prediction`, `scikit-learn`, `Web App`
