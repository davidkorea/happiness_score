import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv('../data_pd/pm2.csv')
data_df.dropna(inplace=True)
data_df['Level'] = pd.cut(data_df['PM'],bins=[0,50,100,500],
                          labels=['Excellent','Good','Bad'])
# grouped_df = data_df.groupby(by=['Year','Month','Day'])['Level'].count()
pivot_df = pd.pivot_table(data_df,index='Year',columns=['Level'],values=['Day'],
                          aggfunc='count')
pivot_df.plot(kind='bar',stacked=True,rot=0,title='2013-2015 PM2.5 Level')
plt.legend()
plt.tight_layout()
plt.savefig('./pm2.5_stacked.png')
plt.show()