import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data_dataset.csv")

# 1. Show dataset structure
print("DATA INFO")
print(df.head())
print(df.columns)
print(df.describe())
print(df.sample(30))

# 2. Check missing values
print("MISSING VALUES")
print(df.isnull().sum())

# Fill missing Notes
df["Notes"] = df["Notes"].fillna("No remarks")

# 3. Remove Notes column
df = df.drop("Notes", axis=1)

# Remove rows with missing Price or Quantity
df = df.dropna(subset=["Price", "Quantity"])

# 4. Sort by Price
df = df.sort_values("Price")

# 5. Filtering

# Price > 500 and Quantity >= 2
print(df[(df["Price"] > 500) & (df["Quantity"] >= 2)])

# Region = North
print(df[df["Region"] == "North"])

# Electronics + Discount >=10 + Quantity >=2
print(df[(df["Category"] == "Electronics") &
         (df["Discount"] >= 10) &
         (df["Quantity"] >= 2)])

# 6. Create new columns
df["TotalAmount"] = df["Price"] * df["Quantity"]
df["DiscountedPrice"] = df["TotalAmount"] - (df["TotalAmount"] * df["Discount"] / 100)

# 7. First name, last name, year

df["FirstName"] = df["CustomerName"].str.split().str[0]
df["LastName"] = df["CustomerName"].str.split().str[1]

df["FirstName"] = df["FirstName"].str.upper()
df["LastName"] = df["LastName"].str.upper()

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Year"] = df["OrderDate"].dt.year

# 8. Grouping

print("Total Sales per Category")
print(df.groupby("Category")["TotalAmount"].sum())

print("Average per Region")
print(df.groupby("Region")["TotalAmount"].mean())

print("Top Region")
print(df.groupby("Region")["TotalAmount"].mean().idxmax())

print("Product with Highest Avg Discount")
print(df.groupby("Product")["Discount"].mean().idxmax())

print("Customer Frequency")
print(df["CustomerName"].value_counts())

# 9. OrderCategory

def order_category(x):
    if x > 3000:
        return "High Value"
    elif x > 1500:
        return "Medium Value"
    else:
        return "Low Value"

df["OrderCategory"] = df["TotalAmount"].apply(order_category)

# 10. DiscountLabel

def discount_label(x):
    if x == 0:
        return "No Discount"
    elif x <= 10:
        return "Low Discount"
    else:
        return "High Discount"

df["DiscountLabel"] = df["Discount"].apply(discount_label)

# Save file
df.to_csv("cleaned_sales_data.csv", index=False)

print("DONE")