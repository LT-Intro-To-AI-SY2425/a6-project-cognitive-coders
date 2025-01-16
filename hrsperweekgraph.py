import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loads and preprocesses the data
data = pd.read_csv("data.csv")
data["income"].replace(["<=50K", ">50K"], [0, 1], inplace=True)

# Groups the data by hours-per-week and income
hours_income_grouped = data.groupby(["hours-per-week", "income"]).size().unstack(fill_value=0)

# Extracts the data for plotting
hours = hours_income_grouped.index
less_than_50k = hours_income_grouped[0]
more_than_50k = hours_income_grouped[1]

#The double bar graph itself
plt.figure(figsize=(14, 8))
width = 0.4
x = range(len(hours))

plt.bar(x, less_than_50k, width=width, label="<=50K", color="blue", alpha=0.7)
plt.bar([i + width for i in x], more_than_50k, width=width, label=">50K", color="orange", alpha=0.7)

# Labels, title, and legend
plt.title("Income Distribution by Hours Worked Per Week", fontsize=16)
plt.xlabel("Hours Worked Per Week", fontsize=14)
plt.ylabel("Number of People", fontsize=14)
plt.xticks([i + width / 2 for i in x], hours, rotation=90)
plt.legend(title="Income", fontsize=12)
plt.grid(alpha=0.3)

# X-axis range
plt.xlim(20, 60) 

# Showing the plot itself
plt.tight_layout()
plt.show()