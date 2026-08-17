
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load raw dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Create copy
cleaned_df = df.copy()

# Handle missing values
cleaned_df["Age"] = cleaned_df["Age"].fillna(
    cleaned_df["Age"].median()
)

cleaned_df["Embarked"] = cleaned_df["Embarked"].fillna(
    cleaned_df["Embarked"].mode()[0]
)

cleaned_df.drop(columns=["Cabin"], inplace=True)

# Remove duplicates
cleaned_df.drop_duplicates(inplace=True)

# Correct data types
cleaned_df["PassengerId"] = cleaned_df["PassengerId"].astype(int)
cleaned_df["Survived"] = cleaned_df["Survived"].astype(int)
cleaned_df["Pclass"] = cleaned_df["Pclass"].astype(int)
cleaned_df["Age"] = cleaned_df["Age"].astype(float)
cleaned_df["SibSp"] = cleaned_df["SibSp"].astype(int)
cleaned_df["Parch"] = cleaned_df["Parch"].astype(int)
cleaned_df["Fare"] = cleaned_df["Fare"].astype(float)

# Treat outliers using IQR capping
numerical_columns = ["Age", "SibSp", "Parch", "Fare"]

for column in numerical_columns:
    Q1 = cleaned_df[column].quantile(0.25)
    Q3 = cleaned_df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    cleaned_df[column] = cleaned_df[column].clip(
        lower=lower_limit,
        upper=upper_limit
    )

# Encode categorical variables
cleaned_df["Sex"] = cleaned_df["Sex"].map({
    "male": 0,
    "female": 1
})

cleaned_df = pd.get_dummies(
    cleaned_df,
    columns=["Embarked"],
    dtype=int
)

# Remove unnecessary text columns
cleaned_df.drop(
    columns=["Name", "Ticket"],
    inplace=True
)

# Standardize numerical columns
scaler = StandardScaler()

columns_to_scale = [
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

cleaned_df[columns_to_scale] = scaler.fit_transform(
    cleaned_df[columns_to_scale]
)

# Rename columns
cleaned_df.rename(columns={
    "PassengerId": "passenger_id",
    "Survived": "survived",
    "Pclass": "passenger_class",
    "Sex": "sex",
    "Age": "age",
    "SibSp": "siblings_spouses",
    "Parch": "parents_children",
    "Fare": "fare",
    "Embarked_C": "embarked_c",
    "Embarked_Q": "embarked_q",
    "Embarked_S": "embarked_s"
}, inplace=True)

# Save cleaned dataset
cleaned_df.to_csv(
    "titanic_cleaned.csv",
    index=False
)

print("Preprocessing completed successfully.")
print("Final shape:", cleaned_df.shape)
