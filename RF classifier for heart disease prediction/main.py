#v2

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    filename = "data.csv"

    # 1) Load the CSV directly into a DataFrame
    df = pd.read_csv(filename)

    # 2) Convert numerical columns from string to float
    numeric_cols = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']
    for col in numeric_cols:
        df[col] = df[col].astype(float)

    # 3) One-hot encoding for categorical columns
    categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # 4) Separate features (X) and target (y)
    X = df.drop('HeartDisease', axis=1)
    y = df['HeartDisease']

    # 5) Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

    # 6) Train Random Forest
    clf = RandomForestClassifier(n_estimators=150, random_state= 42)
    clf.fit(X_train, y_train)

    # 7) Predict and evaluate
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nRandom Forest Classifier Accuracy: {accuracy:.3f}")
