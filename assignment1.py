import pandas as pd

# =========================
# Load Dataset
# =========================
df = pd.read_csv("student_data.csv")


# =========================================================
# 1. Dataset Structure, Summary, Columns, Types, Shape, Sample 30
# =========================================================
print("\n--- DATASET STRUCTURE ---")
print(df.head())

print("\n--- SUMMARY STATISTIC ---")
print(df.describe(include='all'))

print("\n--- LIST OF COLUMNS ---")
print(df.columns)

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- NUMBER OF ROWS AND COLUMNS ---")
print(df.shape)

print("\n--- RANDOM 30 DATA ---")
print(df.sample(30))


# =========================================================
# 2. Duplicates
# =========================================================
print("\n--- DUPLICATE COUNT ---")
print(df.duplicated().sum())

print("\n--- DUPLICATE ROWS ---")
print(df[df.duplicated()])

df = df.drop_duplicates()


# =========================================================
# 3. Missing Values Handling
# =========================================================
print("\n--- MISSING VALUES PER COLUMN ---")
print(df.isnull().sum())

# Fill Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill Score with median
df["Score"] = df["Score"].fillna(df["Score"].median())

# Fill Attendance with forward fill (row)
df["Attendance"] = df["Attendance"].ffill()


# =========================================================
# 4. Replace Values (IT & CS)
# =========================================================
df["Department"] = df["Department"].replace({
    "IT": "Information Technology",
    "CS": "Computer Science"
})


# =========================================================
# 5. Change Age to INT and verify
# =========================================================
df["Age"] = df["Age"].astype(int)

print("\n--- AGE DATA TYPE AFTER CONVERSION ---")
print(df["Age"].dtype)


# =========================================================
# 6. Drop StudentID
# =========================================================
df = df.drop(columns=["StudentID"])


# =========================================================
# 7. Create Grade Column using apply()
# =========================================================
def get_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    else:
        return "Average"

df["Grade"] = df["Score"].apply(get_grade)


# =========================================================
# 8. Show all rows and structure
# =========================================================
print("\n--- ALL ROWS IN DATASET ---")
print(df)

print("\n--- FINAL STRUCTURE ---")
print(df.info())