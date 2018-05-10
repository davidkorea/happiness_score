import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def collect_data():
    data_df = pd.read_csv('./data_pd/happiness_report.csv')
    return data_df

def process_data(data_df):
    data_df.dropna(inplace=True)
    data_df.sort_values(['Year','Happiness Score'], ascending=[True,False],inplace=True)
    return data_df

def analyse_data(data_df):
    # 1 apply()
    # def score2level(var):
    #     if var <= 3:
    #         level = 'Low'
    #     elif var <=5:
    #         level = 'Middle'
    #     else:
    #         level = 'High'
    #     return level
    #
    # data_df['Level'] = data_df['Happiness Score'].apply(score2level)

    # 2 cut()
    data_df['Level'] = pd.cut(data_df['Happiness Score'],
                              bins=[-np.inf,3,5,np.inf],
                              labels=['Low','Middle','High'])
    pivot_df = pd.pivot_table(data_df, index='Region',columns=['Year','Level'],
                              values=['Country'],aggfunc='count')
    # values=[''] must be a [], or couldn't plot
    pivot_df.fillna(0,inplace=True)
    # print(pivot_df)
    return pivot_df

def plot(pivot_df):
    for year in [2015,2016,2017]:
        pivot_df['Country',year].plot(kind='bar',stacked=True,
                                      title='Happiness Level of {}'.format(year))
        plt.tight_layout()
        plt.legend(loc='best')
        plt.savefig('./pivot_{}.png'.format(year))
        plt.show()

def main():
    data_df = collect_data()
    data_df = process_data(data_df)

    pivot_df = analyse_data(data_df)
    plot(pivot_df)

main()