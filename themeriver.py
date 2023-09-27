import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('agg_new_data.csv', parse_dates={'date':['tweet_time','tweet_time.1','tweet_time.2']})

labels = df.columns[1:-1]

values = []

for i in df.columns[1:-1]:
    x = df[i].values()
    values.append(x)

x = df.date.values()
y1 = values[0]
y2 = values[1]
y3 = values[2]
y4 = values[3]
y5 = values[4]
y6 = values[5]
y7 = values[6]
y8 = values[7]
y9 = values[8]
y10 = values[9]
y11 = values[10]
y12 = values[11]

plt.figure()
plt.stackplot(x, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, labels = labels, baseline='sym')
plt.legend(loc='upper left')
plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.title('Themeriver')
plt.ylim(100,100)
plt.figsize(20,10)
plt.show()