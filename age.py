import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the data
data = pd.read_csv("data.csv")
data["income"].replace(["<=50K", ">50K"], [0, 1], inplace=True)

# Group the data by age and income
age_income_grouped = data.groupby(["Age", "income"]).size().unstack(fill_value=0)

# Extract data for plotting
ages = age_income_grouped.index
less_than_50k = age_income_grouped[0]
more_than_50k = age_income_grouped[1]

# Create the double bar graph
plt.figure(figsize=(14, 8))
width = 0.4
x = range(len(ages))

plt.bar(x, less_than_50k, width=width, label="<=50K", color="blue", alpha=0.7)
plt.bar([i + width for i in x], more_than_50k, width=width, label=">50K", color="orange", alpha=0.7)

# Add labels, title, and legend
plt.title("Income Distribution by Age", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Number of People", fontsize=14)
plt.xticks([i + width / 2 for i in x], ages, rotation=90)
plt.legend(title="Income", fontsize=12)
plt.grid(alpha=0.3)

# Set the x-axis range
plt.xlim(18, 60)  # Adjust these values as needed

# Show the plot
plt.tight_layout()
plt.show()