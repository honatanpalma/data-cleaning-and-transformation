## Data Cleaning and Transformation

This project demonstrates the application of common data cleaning and transformation techniques on a student performance dataset. The goal is to prepare the data for further analysis or machine learning modeling.

## Dataset Overview
The dataset was obtained from Kaggle: https://www.kaggle.com/datasets/haseebindata/student-performance-predictions and contains information about students, including their attendance rate, study hours, previous grades, extracurricular activities, parental support, and final grades.

## Steps Performed

1. **Handling Missing Values**
   - Although the original dataset contained no missing values, the script includes a step to handle them using `df.dropna()`. This ensures robustness in case future datasets have missing data.

2. **Removing Duplicates**
   - Duplicate rows, if any, are removed based on the unique identifier `StudentID`. This prevents any bias or inaccuracies in the analysis due to redundant data.

3. **Normalization**
   - The `AttendanceRate`, `StudyHoursPerWeek`, and `PreviousGrade` columns are normalized using `MinMaxScaler` from scikit-learn. This scales the features to a range of 0-1, making them comparable and potentially improving the performance of machine learning algorithms.

4. **Encoding Categorical Variables**
   - Categorical variables `Gender` and `ParentalSupport` are transformed into numerical representations using one-hot encoding. This enables their inclusion in mathematical computations required for modeling.

5. **Feature Engineering**
   - A new feature, `GradeImprovement`, is calculated by subtracting `PreviousGrade` from `FinalGrade`. This derived feature provides direct insight into the academic progress of each student.

## Code and Implementation

The Python script utilizes the Pandas library for data manipulation and scikit-learn for preprocessing.
