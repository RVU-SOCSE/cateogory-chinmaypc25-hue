import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df4 = pd.read_csv(r"C:\Users\chinm\Desktop\Python\3Salary_Data.csv")
plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5)
plt.show()
sns.barplot(x=df4['experience_level'], y=df4['salary_in_usd'])
