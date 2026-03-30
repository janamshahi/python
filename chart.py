import matplotlib.pyplot as plt
import numpy as np

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 180, 200]
expenses = [100, 130, 120, 150, 160, 170]
profit = [s - e for s, e in zip(sales, expenses)]

categories = ["IT", "HR", "Sales", "Marketing"]
values = [40, 15, 30, 15]

# Create Dashboard Layout
plt.figure(figsize=(12, 8))

# 🔹 1. Line Chart (Sales vs Expenses)
plt.subplot(2, 2, 1)
plt.plot(months, sales, marker='o', label="Sales")
plt.plot(months, expenses, marker='o', linestyle='--', label="Expenses")
plt.title("Sales vs Expenses")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.grid()

# 🔹 2. Bar Chart (Profit)
plt.subplot(2, 2, 2)
plt.bar(months, profit)
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit")

# 🔹 3. Pie Chart (Department Share)
plt.subplot(2, 2, 3)
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Department Distribution")

# 🔹 4. Scatter Plot (Sales Trend)
plt.subplot(2, 2, 4)
plt.scatter(months, sales)
plt.title("Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

# Adjust Layout
plt.suptitle("📊 Business Dashboard", fontsize=16)
plt.tight_layout()
plt.show()