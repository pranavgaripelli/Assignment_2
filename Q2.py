import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("D:/Spring/data.csv")
mean_value=df['Calories'].mean()
df['Calories'].fillna(value=mean_value,inplace=True)
df.head(25)
df.Duration.describe()
df.Pulse.describe()
df[(df['Calories']>500) & (df['Calories']<1000)]
df[(df['Calories']>500 & (df['Pulse']<100))]
df_modified=df.drop("Maxpulse",axis=1)
df_modified
df=df.drop("Maxpulse",axis=1)
df
df['Calories']=df['Calories'].astype(int)
df.dtypes
df.plot.scatter( x = 'Duration', y = 'Calories')
plt.show()