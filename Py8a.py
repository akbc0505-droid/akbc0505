import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------
# Create Sample Sales Data
# -----------------------------
data = {
 "years": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
 "Product_A": [12000, 15000, 17000, 16000, 18000, 20000],
 "Product_B": [10000, 12000, 14000, 13000, 15000, 17000],
 "Product_C": [8000, 9000, 10000, 11000, 12000, 14000]
}
df = pd.DataFrame(data)
# -----------------------------
# Line Plot – yearsly Sales
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["years"], df["Product_A"], marker='o', label="Product A")
plt.plot(df["years"], df["Product_B"], marker='o', label="Product B")
plt.plot(df["years"], df["Product_C"], marker='o', label="Product C")
plt.title("yearsly Sales Trend")
plt.xlabel("years")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(True)
plt.show()
# -----------------------------
# Bar Chart – Sales Comparison
# -----------------------------
df.set_index("years").plot(kind="bar", figsize=(8, 5))
plt.title("Sales Comparison by Product")
plt.xlabel("years")
plt.ylabel("Sales Amount")
plt.show()
# -----------------------------
# Pie Chart – Total Sales Share
# -----------------------------
total_sales = df[["Product_A", "Product_B", "Product_C"]].sum()
plt.figure(figsize=(6, 6))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()
# -----------------------------
# Heatmap – Sales Intensity
# -----------------------------
plt.figure(figsize=(8, 5))
sns.heatmap(df.drop("years", axis=1), annot=True, cmap="YlGnBu")
plt.title("Sales Heatmap")
plt.show()
