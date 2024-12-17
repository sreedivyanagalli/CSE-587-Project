# CSE-587-Project
# Combined new dataset with existing(previously used) dataset for better complexity
a. Questions Listed for Each Team Member
    1. Janani chalapati (50592361, jananich@buffalo.edu): Which health factors are the most important for predicting diabetes risk?
    2. Srinischala Alugubelli (50595806, srinisch@buffalo.edu): How do BMI, glucose levels, and blood pressure affect the accuracy of diabetes risk predictions?
    3. Sree Divya Nagalli(50595821, sreedivy@buffalo.edu): Can machine learning do a better job than traditional methods in spotting diabetes risk?
    4. Praveen Kumar Byrapuneni (50593961, pbyrapun@buffalo.edu): How do lifestyle habits, like diet and exercise, influence these predictions?

b. Experiment Code Associated with Each Question
    Health Factors:
    File: app.py, class HealthFactorsPredictor.
    Line: Functions using RandomForestClassifier.
    Demographic Factors:
    File: app.py, class DemographicPredictor.
    Line: Functions using AdaBoostClassifier.
    Machine Learning vs Traditional Methods:
    File: app.py, class SocioeconomicPredictor.
    Line: Functions using ExtraTreesClassifier.
    Lifestyle Habits:
    File: app.py, class LifestylePredictor.
    Line: Functions using LogisticRegression.

c. Analysis Location for Each Question
The analysis for each hypothesis question is present in: app.py for implementation.
The associated metrics and results are discussed in the report in Sections VII (Evaluation Metrics) and VIII (Results and Discussions).

d. Folder Structure
app/: Contains all the application code (app.py with imported classifiers and logic for prediction).
exp/: Contains Jupyter notebooks (.ipynb) for running experiments and generating results.
results/: Contains experiment outputs like accuracy scores, ROC-AUC, and confusion matrices.
report/: Documentation including insights, evaluation, and findings (report.pdf).

e. Instructions to Build the App from Source Code
Pre-requisites: Python 3.8 or higher.
Libraries: Install dependencies using pip install -r requirements.txt.
Setting Up the Environment: Clone the repository or unzip the project files. Navigate to the project directory.
Running the Application: Run the app.py file using the command: python app.py(This will start the application, allowing users to input data and receive predictions.)
Testing:
To test the application, navigate to exp/ and run the .ipynb files for individual model evaluations.
