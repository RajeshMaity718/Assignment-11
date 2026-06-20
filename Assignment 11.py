import matplotlib.pyplot as plt
import numpy as np

# ==================================================
# Task 1: Line Plot (Sales Trend)
# ==================================================

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1800, 1700, 2100, 2500]

plt.figure()
plt.plot(months, sales)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


# ==================================================
# Task 2: Scatter Plot
# ==================================================

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [40, 50, 55, 65, 70, 75, 85, 95]

plt.figure()
plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()


# ==================================================
# Task 3: Bar Plot (Vertical & Horizontal)
# ==================================================

products = ['Laptop', 'Mobile', 'Tablet', 'Watch']
product_sales = [50, 80, 30, 40]

# Vertical Bar Chart
plt.figure()
plt.bar(products, product_sales)

plt.title("Product Sales (Vertical Bar Chart)")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.show()

# Horizontal Bar Chart
plt.figure()
plt.barh(products, product_sales)

plt.title("Product Sales (Horizontal Bar Chart)")
plt.xlabel("Units Sold")
plt.ylabel("Products")
plt.show()


# ==================================================
# Task 4: Multiple Bar Plot
# ==================================================

products = ['Laptop', 'Mobile', 'Tablet']

sales_2024 = [50, 80, 40]
sales_2025 = [70, 90, 60]

x = np.arange(len(products))
width = 0.35

plt.figure()
plt.bar(x - width/2, sales_2024, width, label='2024')
plt.bar(x + width/2, sales_2025, width, label='2025')

plt.xticks(x, products)

plt.title("Sales Comparison (2024 vs 2025)")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()

plt.show()


# ==================================================
# Task 5: Stacked Bar Chart
# ==================================================

months = ['Jan', 'Feb', 'Mar', 'Apr']

online_sales = [100, 120, 140, 160]
offline_sales = [80, 100, 90, 110]

plt.figure()
plt.bar(months, online_sales, label='Online Sales')
plt.bar(months, offline_sales,
        bottom=online_sales,
        label='Offline Sales')

plt.title("Online and Offline Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.show()


# ==================================================
# Task 6: Histogram (Marks Distribution)
# ==================================================

student_marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.figure()
plt.hist(student_marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()


# ==================================================
# Task 7: Pie Chart (Market Share)
# ==================================================

companies = ['A', 'B', 'C', 'D']
market_share = [35, 25, 20, 20]

plt.figure()
plt.pie(
    market_share,
    labels=companies,
    autopct='%1.1f%%'
)

plt.title("Market Share Distribution")

plt.show()
