# Exam Success Analytics for Scholarships

This project provides a web application for predicting whether a student will receive a scholarship based on various academic and extracurricular features. The model is built using machine learning algorithms like Gradient Boosting and Random Forest, and it handles class imbalance using SMOTE. The app is developed using Streamlit for easy deployment.

## Project Pipeline

### 1. Data Collection
- A dataset containing student information (scores, extracurricular activities) is used for training the model.
  
### 2. Data Preprocessing
- Clean and prepare data by handling missing values.
- Create additional features such as interaction terms (e.g., `Math_Science_Interaction`).
- Normalize continuous features (e.g., `Math_Score`, `Science_Score`).
  
### 3. Feature Engineering
- Create new interaction features to capture relationships between different subjects.
- Convert categorical features into numeric values using `LabelEncoder` and one-hot encoding.
  
### 4. Class Imbalance Handling
- Use techniques like **SMOTE** (Synthetic Minority Over-sampling Technique) to handle imbalanced classes and ensure the model has enough examples of both classes (won a scholarship vs. did not win).

### 5. Model Selection
- Use machine learning classifiers like **Random Forest** and **Gradient Boosting** to predict whether a student wins a scholarship or not.
  
### 6. Model Tuning
- Use **GridSearchCV** to tune hyperparameters such as `n_estimators`, `max_depth`, and `learning_rate` to optimize model performance.

### 7. Model Evaluation
- Evaluate models using standard classification metrics such as **accuracy**, **precision**, **recall**, **F1-score**, and confusion matrices to assess the model's performance on the test set.
  
### 8. Streamlit Web Application
- The model is deployed using **Streamlit**, where users can input their academic data, and the model predicts the likelihood of them receiving a scholarship.

## Features

- **Math Score**
- **Science Score**
- **English Score**
- **Hours Studied**
- **Extracurricular Activities**

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/minalmmm/Exam-Success-Analytics-for-Scholarships.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

4. Enter student data (scores, extracurricular activities, etc.) into the form and click "Predict Scholarship" to get the result.

## Output Image

![Scholarship Prediction Output](https://github.com/minalmmm/Exam-Success-Analytics-for-Scholarships/blob/main/images/img2.png)
![Scholarship Prediction Output](https://github.com/minalmmm/Exam-Success-Analytics-for-Scholarships/blob/main/images/img1.png)

## Model Used

The app uses the following models:
- **Random Forest Classifier**
- **Gradient Boosting Classifier**

The models are trained and tuned to predict whether a student is likely to win a scholarship based on their performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

