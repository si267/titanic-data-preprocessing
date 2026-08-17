# Titanic Data Preprocessing

This project demonstrates data preprocessing techniques using the Titanic dataset. The dataset was obtained from Kaggle and preprocessing was performed using Python in Google Colab.

## 1. Dataset Source

- Dataset: Titanic Dataset
- Source: Kaggle
- Dataset type: CSV
- Original dataset: `data/raw/titanic_raw.csv`

## 2. Dataset Description

The Titanic dataset contains information about passengers who travelled on the RMS Titanic. It includes passenger details such as passenger class, name, gender, age, number of siblings/spouses, number of parents/children, ticket, fare, cabin and port of embarkation.

## 3. Dataset Before Preprocessing

- Number of rows: **891**
- Number of columns: **12**

### Original columns

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

## 4. Problems Identified

The following issues were identified during inspection of the raw dataset:

- Missing values in `Age`
- Missing values in `Cabin`
- Missing values in `Embarked`
- Duplicate rows were checked
- Outliers were present in numerical variables
- Categorical variables were present
- Numerical variables required standardization
- Column names required consistent formatting

## 5. Preprocessing Techniques Applied

### 5.1 Handling Missing Values

- Missing values in `Age` were replaced using the median.
- Missing values in `Embarked` were replaced using the mode.
- The `Cabin` column was removed because it contained a large number of missing values.

### 5.2 Removing Duplicates

Duplicate rows were checked and removed from the dataset.

No passenger records were deleted because of duplicate rows.

### 5.3 Outlier Detection and Treatment

Outliers were detected using the **Interquartile Range (IQR)** method.

The following numerical columns were checked:

- Age
- SibSp
- Parch
- Fare

Extreme values were treated using **IQR capping** rather than deleting rows.

### 5.4 Data Type Correction

Numerical columns were converted to appropriate numerical data types such as integer and floating-point types.

### 5.5 Categorical Variable Encoding

The `Sex` column was converted into numerical values:

- Male → 0
- Female → 1

The `Embarked` column was converted using one-hot encoding.

### 5.6 Removing Unnecessary Text Columns

The following high-cardinality text columns were removed:

- Name
- Ticket

### 5.7 Numerical Standardization

The following numerical columns were standardized using `StandardScaler`:

- Age
- SibSp
- Parch
- Fare

### 5.8 Column Renaming

Column names were renamed into a consistent lowercase format with descriptive names.

## 6. Dataset After Preprocessing

- Number of rows: **891**
- Number of columns: **11**

The cleaned dataset contains no remaining missing values.

## 7. Files in This Repository

```text
data/
├── raw/
│   └── titanic_raw.csv
│
└── cleaned/
    └── titanic_cleaned.csv

preprocessing.py
README.md
The final cleaned dataset contains 891 rows and 11 columns.
