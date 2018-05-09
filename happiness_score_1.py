import pandas as pd
import matplotlib.pyplot as plt



def collect_data():
    data_df = pd.read_csv('./data_pd/happiness_report.csv')
    return data_df

def process_data(data_df):
    # data_df.groupby(by=['Year','Region'])
    # ['Happiness Score','Economy (GDP per Capita)'].mean()
    data_df.dropna(inplace=True)
    data_df.sort_values(['Year','Happiness Score'], ascending=[True,False],inplace=True)
    return data_df

def analyse_data(data_df):
    grouped_results = data_df.groupby(by=['Year','Region'])['Happiness Score'].mean()
    pivot_results = pd.pivot_table(data_df, index='Region', columns='Year',
                                   values=['Happiness Score', 'Economy (GDP per Capita)'],
                                   aggfunc='mean')
    return grouped_results,pivot_results

def plot(grouped_results,pivot_results):
    # grouped_results.plot()
    # plt.show()
    pivot_results['Happiness Score'].plot(kind='bar',title='Happiness Score')
    plt.tight_layout()
    plt.show()
    pivot_results['Economy (GDP per Capita)'].plot(kind='bar',title='Economy (GDP per Capita)')
    plt.tight_layout()
    plt.show()

def main():
    data_df = collect_data()
    data_df = process_data(data_df)
    grouped_results, pivot_results = analyse_data(data_df)
    plot(grouped_results,pivot_results)
main()