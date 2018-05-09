import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv('../data_pd/pm2.csv')
data_df.dropna(inplace=True)
grouped_df = data_df.groupby(by=['Year','Month'])['PM'].mean()
# print(grouped_df.head(10))
pivot_df = pd.pivot_table(data_df,index='Year',columns='Month',values='PM',aggfunc='mean')
# pivot used to make grouped bar plot?
pivot_df.plot(kind='bar',rot=0,title='2013-2015 PM2.5 Monthly Report')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('./pm2.5_1.png')
plt.show()