# ============================================================
# NEXORA TECHNOLOGIES
# WEEK 3 — DATA ANALYSIS & FEATURE ENGINEERING WITH PANDAS
# SESSION 5 — PANDAS DATAFRAMES & DATA WRANGLING
# ============================================================

# SESSION DURATION: 2 HOURS
#
# Main goal:
# By the end of this session, you should understand how to:
# 1. Work with Pandas Series and DataFrames
# 2. Create and inspect datasets
# 3. Import CSV files
# 4. Understand missing values
# 5. Clean messy data
# 6. Filter data
# 7. Group and summarize data
# 8. Create new features from existing columns
# 9. Extract useful insights from a dataset
#
# IMPORTANT:
# We are learning by DOING.
# Don't just read the code. Type it and run it.
# ============================================================


# ============================================================
# 00:00 - 00:10
# 1. WHAT IS PANDAS?
# ============================================================

# Pandas is a Python library used for:
#
# - Working with tables of data
# - Cleaning data
# - Analyzing data
# - Preparing data for Machine Learning
# - Reading CSV and Excel files
#
# Think of Pandas as something similar to:
#
#       Excel + Python
#
# Instead of manually working with thousands of rows,
# Python can process them for us.


# ------------------------------------------------------------
# INSTALLING PANDAS
# ------------------------------------------------------------

# In your VS Code terminal, run:
#
# pip install pandas
#
# If you also want to work with Excel files:
#
# pip install openpyxl


# ------------------------------------------------------------
# IMPORTING PANDAS
# ------------------------------------------------------------

import pandas as pd

# "pd" is simply a short name we normally use for Pandas.
#
# Instead of writing:
#
# pandas.DataFrame()
#
# we can write:
#
# pd.DataFrame()


# ============================================================
# 00:10 - 00:25
# 2. PANDAS SERIES
# ============================================================

# A Series is basically a single column of data.

names = pd.Series(["John", "Mary", "Peter", "Alice"])

print(names)


# You can also create a Series of numbers.

ages = pd.Series([20, 22, 19, 25])

print(ages)


# Each value has an index.
#
# Example:
#
# 0    John
# 1    Mary
# 2    Peter
# 3    Alice
#
# The numbers on the left are indexes.


# Accessing one value:

print(names[0])

# Output:
# John


print(names[2])

# Output:
# Peter


# ============================================================
# QUICK CHECK
# ============================================================

# Ask yourself:
#
# What is a Series?
#
# Answer:
# A Series is a one-dimensional labeled data structure.
#
# For beginners:
# Think of it as ONE column of data.


# ============================================================
# 00:25 - 00:45
# 3. PANDAS DATAFRAME
# ============================================================

# A DataFrame is a table.
#
# Think about an Excel spreadsheet:
#
# Name      Age     Country
# John      20      Kenya
# Mary      22      Uganda
# Peter     19      Kenya
#
# That entire table is a DataFrame.


# ------------------------------------------------------------
# CREATING A DATAFRAME
# ------------------------------------------------------------

data = {
    "Name": ["John", "Mary", "Peter", "Alice"],
    "Age": [20, 22, 19, 25],
    "Country": ["Kenya", "Uganda", "Kenya", "Tanzania"]
}

df = pd.DataFrame(data)

print(df)


# ------------------------------------------------------------
# UNDERSTANDING THE CODE
# ------------------------------------------------------------

# data = {...}
#
# We created a Python dictionary.
#
# Each dictionary key becomes a column.
#
# "Name"    -> column
# "Age"     -> column
# "Country" -> column
#
# pd.DataFrame(data)
#
# converts our dictionary into a table.


# ============================================================
# ACCESSING COLUMNS
# ============================================================

print(df["Name"])

print(df["Age"])

print(df["Country"])


# We can also access multiple columns:

print(df[["Name", "Age"]])


# ============================================================
# ACCESSING ROWS
# ============================================================

# iloc allows us to access rows by position.

print(df.iloc[0])

# First row


print(df.iloc[2])

# Third row


# Multiple rows:

print(df.iloc[0:2])


# ============================================================
# 3 IMPORTANT COMMANDS
# ============================================================

# head()
# Shows the first 5 rows.

print(df.head())


# tail()
# Shows the last 5 rows.

print(df.tail())


# info()
# Gives information about the dataset.

df.info()


# ============================================================
# CHECKING THE SIZE OF DATA
# ============================================================

print(df.shape)

# Example:
#
# (4, 3)
#
# 4 = number of rows
# 3 = number of columns


# ============================================================
# CHECKING COLUMN NAMES
# ============================================================

print(df.columns)


# ============================================================
# 00:45 - 01:00
# 4. IMPORTING CSV DATA
# ============================================================

# In real projects, we normally don't manually create
# the dataset.
#
# We receive data from:
#
# - CSV files
# - Excel files
# - Databases
# - APIs
# - Websites
# - Applications


# ------------------------------------------------------------
# READING A CSV FILE
# ------------------------------------------------------------

# Example:
#
# df = pd.read_csv("customers.csv")


# If the CSV file is inside the same folder as your Python file:
#
# pd.read_csv("customers.csv")


# If it is inside a folder:
#
# pd.read_csv("data/customers.csv")


# ------------------------------------------------------------
# READING EXCEL
# ------------------------------------------------------------

# df = pd.read_excel("customers.xlsx")


# ============================================================
# IMPORTANT
# ============================================================

# When teaching this section:
#
# CSV = Comma-Separated Values
#
# Example CSV:
#
# Name,Age,Country
# John,20,Kenya
# Mary,22,Uganda
# Peter,19,Kenya
#
# Pandas converts this into a DataFrame.


# ============================================================
# 01:00 - 01:15
# 5. UNDERSTANDING MISSING VALUES
# ============================================================

# Real-world datasets are often messy.
#
# Example:
#
# Name      Age     Salary
# John      21      30000
# Mary      NaN     40000
# Peter     25      NaN
#
# NaN means:
#
# Not a Number / missing value.


# Let's create a messy dataset.

data = {
    "Name": ["John", "Mary", "Peter", "Alice", "David"],
    "Age": [21, None, 25, 23, None],
    "Salary": [30000, 40000, None, 35000, 45000]
}

df = pd.DataFrame(data)

print(df)


# ------------------------------------------------------------
# FINDING MISSING VALUES
# ------------------------------------------------------------

print(df.isnull())


# This shows True where data is missing.


# Count missing values in every column:

print(df.isnull().sum())


# Example output:
#
# Name       0
# Age        2
# Salary     1


# ============================================================
# DEALING WITH MISSING VALUES
# ============================================================

# Method 1:
# Remove rows containing missing values.

clean_df = df.dropna()

print(clean_df)


# WARNING:
#
# dropna() removes rows.
#
# In real projects, don't automatically delete data.
# First understand WHY the values are missing.


# ------------------------------------------------------------
# METHOD 2: FILL MISSING VALUES
# ------------------------------------------------------------

# We can replace missing ages with the average age.

average_age = df["Age"].mean()

print(average_age)


df["Age"] = df["Age"].fillna(average_age)

print(df)


# Now missing ages have been replaced.


# ============================================================
# 01:15 - 01:30
# 6. FILTERING DATA
# ============================================================

# Filtering means selecting only rows
# that satisfy a condition.


# Example:

data = {
    "Name": ["John", "Mary", "Peter", "Alice", "David"],
    "Age": [21, 30, 25, 19, 35],
    "Salary": [30000, 50000, 40000, 25000, 70000]
}

df = pd.DataFrame(data)


# Find people older than 25:

result = df[df["Age"] > 25]

print(result)


# Find people earning more than 40,000:

result = df[df["Salary"] > 40000]

print(result)


# Find people exactly 25:

result = df[df["Age"] == 25]

print(result)


# ============================================================
# USING AND
# ============================================================

# Example:
#
# Age greater than 20
# AND
# Salary greater than 30,000


result = df[
    (df["Age"] > 20) &
    (df["Salary"] > 30000)
]

print(result)


# & means AND in Pandas conditions.


# ============================================================
# USING OR
# ============================================================

result = df[
    (df["Age"] < 20) |
    (df["Age"] > 30)
]

print(result)

# | means OR.


# ============================================================
# 01:30 - 01:45
# 7. GROUPBY
# ============================================================

# groupby() allows us to group similar data.
#
# Example:
#
# We have customers from different countries.
#
# We want to know the average salary for each country.


data = {
    "Name": ["John", "Mary", "Peter", "Alice", "David", "Sarah"],
    "Country": [
        "Kenya",
        "Kenya",
        "Uganda",
        "Uganda",
        "Kenya",
        "Tanzania"
    ],
    "Salary": [
        30000,
        40000,
        35000,
        45000,
        50000,
        32000
    ]
}

df = pd.DataFrame(data)


# Group by country:

grouped = df.groupby("Country")

print(grouped["Salary"].mean())


# This tells us:
#
# Average salary for Kenya
# Average salary for Uganda
# Average salary for Tanzania


# ============================================================
# AGGREGATION
# ============================================================

# Aggregation means summarizing data.


# Average:

print(df["Salary"].mean())


# Maximum:

print(df["Salary"].max())


# Minimum:

print(df["Salary"].min())


# Total:

print(df["Salary"].sum())


# Number of records:

print(df["Salary"].count())


# ============================================================
# MULTIPLE AGGREGATIONS
# ============================================================

summary = df.groupby("Country")["Salary"].agg(
    ["mean", "max", "min", "count"]
)

print(summary)


# This gives us several statistics at once.


# ============================================================
# 01:45 - 01:55
# 8. FEATURE ENGINEERING
# ============================================================

# Feature engineering means creating NEW useful columns
# from existing data.
#
# This is extremely important in Machine Learning.


# Example:

data = {
    "Name": ["John", "Mary", "Peter"],
    "Age": [20, 25, 30],
    "MonthlySalary": [30000, 40000, 50000]
}

df = pd.DataFrame(data)


# Create annual salary:

df["AnnualSalary"] = df["MonthlySalary"] * 12

print(df)


# We created a new feature:
#
# AnnualSalary


# ------------------------------------------------------------
# ANOTHER FEATURE
# ------------------------------------------------------------

# Create an age category.

df["Adult"] = df["Age"] >= 18

print(df)


# True = 18 or older
# False = below 18


# ============================================================
# WHY FEATURE ENGINEERING?
# ============================================================

# Raw data is not always enough.
#
# We transform existing information into something
# that may be more useful for analysis or Machine Learning.
#
# Example:
#
# MonthlySalary
#
# becomes
#
# AnnualSalary
#
# This can make analysis easier.


# ============================================================
# 01:55 - 02:00
# 9. FINAL MINI PROJECT
# ============================================================

# PROJECT:
# CUSTOMER ANALYSIS
#
# We will create a small customer dataset,
# clean it, analyze it, and create new features.


customers = {
    "Name": [
        "John",
        "Mary",
        "Peter",
        "Alice",
        "David",
        "Sarah"
    ],

    "Age": [
        21,
        None,
        30,
        25,
        None,
        35
    ],

    "MonthlySpend": [
        5000,
        7000,
        None,
        4000,
        9000,
        6000
    ],

    "Country": [
        "Kenya",
        "Kenya",
        "Uganda",
        "Kenya",
        "Uganda",
        "Tanzania"
    ]
}

df = pd.DataFrame(customers)


# ------------------------------------------------------------
# STEP 1: INSPECT THE DATA
# ------------------------------------------------------------

print(df.head())

print(df.info())

print(df.shape)


# ------------------------------------------------------------
# STEP 2: CHECK MISSING VALUES
# ------------------------------------------------------------

print(df.isnull().sum())


# ------------------------------------------------------------
# STEP 3: FILL MISSING AGE
# ------------------------------------------------------------

average_age = df["Age"].mean()

df["Age"] = df["Age"].fillna(average_age)


# ------------------------------------------------------------
# STEP 4: FILL MISSING SPENDING
# ------------------------------------------------------------

average_spending = df["MonthlySpend"].mean()

df["MonthlySpend"] = df["MonthlySpend"].fillna(
    average_spending
)


# ------------------------------------------------------------
# STEP 5: CREATE NEW FEATURE
# ------------------------------------------------------------

df["AnnualSpend"] = df["MonthlySpend"] * 12


# ------------------------------------------------------------
# STEP 6: CREATE CUSTOMER CATEGORY
# ------------------------------------------------------------

df["HighSpender"] = df["MonthlySpend"] > 6000


# ------------------------------------------------------------
# STEP 7: FILTER HIGH SPENDERS
# ------------------------------------------------------------

high_spenders = df[
    df["HighSpender"] == True
]

print(high_spenders)


# ------------------------------------------------------------
# STEP 8: GROUP BY COUNTRY
# ------------------------------------------------------------

country_summary = df.groupby("Country")[
    "MonthlySpend"
].mean()

print(country_summary)


# ------------------------------------------------------------
# STEP 9: FINAL DATASET
# ------------------------------------------------------------

print(df)


# ============================================================
# FINAL QUESTIONS
# ============================================================

# Ask the team:
#
# 1. What is a DataFrame?
#
# 2. What is a Series?
#
# 3. How do we read a CSV file?
#
# 4. What does NaN mean?
#
# 5. How can we find missing values?
#
# 6. What does fillna() do?
#
# 7. What does groupby() do?
#
# 8. What is filtering?
#
# 9. What is feature engineering?
#
# 10. Why is feature engineering important in Machine Learning?


# ============================================================
# TAKE-HOME ASSIGNMENT
# ============================================================

# PROJECT: REAL-WORLD DATA CLEANING
#
# Find or use a CSV dataset containing at least:
#
# - 50 rows
# - 4 columns
# - Some missing values
# - At least one numerical column
# - At least one categorical column


# YOUR TASK
#
# 1. Load the CSV using Pandas.
#
# 2. Display the first 5 rows.
#
# 3. Display the last 5 rows.
#
# 4. Display the dataset information.
#
# 5. Find the number of rows and columns.
#
# 6. Find missing values in every column.
#
# 7. Handle the missing values.
#
# 8. Filter the data using at least 2 conditions.
#
# 9. Use groupby() to find a useful summary.
#
# 10. Create TWO new features.
#
# 11. Explain what your two new features mean.
#
# 12. Write at least THREE useful insights
#     you discovered from the dataset.


# ============================================================
# SUBMISSION REQUIREMENTS
# ============================================================

# Submit:
#
# 1. Your Python file
#       session5.py
#
# 2. Your original dataset
#       dataset.csv
#
# 3. Your cleaned dataset
#       cleaned_dataset.csv
#
# 4. A short README containing:
#
#       - Dataset name
#       - What the dataset contains
#       - Problems found
#       - How you cleaned it
#       - Two features you created
#       - Three insights you discovered
#
#
# ============================================================
# NEXORA TECHNOLOGIES
# WEEK 3 — SESSION 5 COMPLETE
# ============================================================
#
# REMEMBER:
#
# DATA → CLEAN → ANALYZE → ENGINEER FEATURES → INSIGHTS
#
# "Don't just look at data. Learn to understand it."
# ============================================================