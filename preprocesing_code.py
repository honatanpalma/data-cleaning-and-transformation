import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read the CSV file into a DataFrame
df = pd.read_csv('student_performance.csv')

# 1. Handle Missing Values
df_cleaned = df.dropna().copy()  # Drop rows with any missing values

# 2. Remove Duplicates
df_cleaned.drop_duplicates(subset='StudentID', inplace=True)  # Drop duplicates based on 'StudentID'

# 3. Normalization
scaler = MinMaxScaler()
df_cleaned[['NormalizedAttendance', 'NormalizedStudyHours', 'NormalizedPreviousGrade']] = scaler.fit_transform(df_cleaned[['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade']])

# 4. Encode Categorical Variables
df_cleaned = pd.get_dummies(df_cleaned, columns=['Gender', 'ParentalSupport'])

# 5. Feature Engineering
df_cleaned['GradeImprovement'] = df_cleaned['FinalGrade'] - df_cleaned['PreviousGrade']

# Display the first 5 rows of the cleaned and transformed DataFrame
print(df_cleaned.head().to_markdown(index=False, numalign="left", stralign="left"))
