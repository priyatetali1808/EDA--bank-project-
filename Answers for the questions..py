import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

df = pd.read_csv ("C:/Users/priya/Downloads/bank-additional.csv")
df.head()
average_balance = df.groupby('job')['loan'].mean().sort_values(ascending=false)
print (average_balance)


#11. average balance 
df.groupby('job')['cons.price.idx'].mean().sort_values(ascending=False)
df.columns

#12. distribution of target variable 

df.groupby('y')['duration'].mean()

#13. average duration of yes or no 

df['y'].value_counts(normalize=True) * 100 

#14. subscription rate by education 
edu_rate = df.groupby('education')['y'].apply(lambda x: (x=='yes').mean() * 100)
print(edu_rate)

#15. barchart - subbscription rate by martial status 
#16.pivot table - clients by job and martial status . 
clients_count = df.pivot_table(index='job',columns='marital',values='nr.employed', aggfunc='count')
print(clients_count)

1#7.contacted the last quater 
subset = df[df['month'].str.lower().isin(['oct', 'nov', 'dec'])]
mean_campaign = subset['campaign'].mean()
print("Mean campaign value for Oct, Nov, Dec:", mean_campaign)

#18.identify strong correlations for numeric columns: 
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(numeric_cols)

#19. poutcome 
df.groupby ('poutcome') ['y'].apply (lambda x: (x=='yes').mean() * 100). sort_values(ascending=False)

#20.	the first 5 rows using the head method. The number of the output rows from the dataset is determined by the head
method parameter.
df = pd.read_csv ("C:/Users/priya/Downloads/bank-additional.csv")
df.head(5)


#21	 dataset size, feature names and their types
shape = df.shape
print(df.shape)
df.tail(5)
#22.	column (feature) names:
df.columns

#23.	DataFrame features (columns), we use the info method:
print(df.info())

#24.We can also set include = all to output statistics on all the existing features.
df.describe(include = ["object"])

#25.	value_counts 
df["y"].value_counts()

#26.	Sorting – Descending order – Duration, age/duration,
df.sort_values(by = "duration", ascending = False).head()

#27. sorting with the descending with the days of the week and month 
df.sort_values(by = ["age", "duration"], ascending = [True, False]).head()
 apply 
df.apply(np.max)

#28.the values ​​replacement in a column by passing it as an argument dictionary in form of {old_value: new_value} .
d = {"no": 0, "yes": 1}
df["y"] = df["y"].map(d)
df.head()

#29.What is the share of clients attracted in our DataFrame?
print("Share of attracted clients =", '{:.1%}'.format(df["y"].mean()))

#30. What are the mean values ​​of numerical features among the attracted clients
df[df["y"] == 1].mean()

#31. What is the average call duration for the attracted clients

acd = round(df[df["y"] == 1]["duration"].mean(), 2)
acd_in_min = acd // 60
print("Average call duration for attracted clients =", acd_in_min, "min", int(acd) % 60, "sec")

#32.  first or last line of the DataFrame
df[-1:]

#33.What is the average age of attracted (y == 1) and unmarried ('marital' == 'single') clients

print("Average age of attracted clients =", int(df[(df["y"] == 1) & (df["marital"] == "single")]["age"].mean()), "years")

#34. Pivot tables

observations.index.name = "y"
observations.columns.name = "marital"
print(observations)

#35. normalizibg the index :
pd.crosstab(df["y"],df["marital"],normalize = 'index')

#36. find the average age and the call duration for different types of client employment job:
average_age = df.pivot_table(["age", "duration"],["job"],aggfunc = "mean" , ).head(10)
print(df(average_age))

#38..List of 10 clients with the largest number of contacts.
df.sort_values(by = "campaign", ascending = False).head(10)

#39.Determine the median age and the number of contacts for different levels of client education.
client_education =  df.pivot_table(["age", "campaign"],["education"],aggfunc = ["mean", "count"])
print(client_education) 











