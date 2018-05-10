# happiness_report

# 1. happiness score
## 1.1 Basic

![](https://github.com/davidkorea/happiness_score/blob/master/images/task.png)

![](https://github.com/davidkorea/happiness_score/blob/master/images/groupby.png)

![](https://github.com/davidkorea/happiness_score/blob/master/images/pivot.png)

## 1.2 Summary

1. collect data
```php
data_df = pd.read_csv('./data_pd/csv')
data_df.dropna(inplace=True)
```
2. sort values - MULTI COLUMNS
```php
data_df.sort_values(['Year','Happiness Score'], ascending=[True,False], inplace=True)
```
3. groupby - MULTI COLUMNS - MULTI-IDNEX
```php
grouped_year_region_df = data_df.groupby(by=['Year','Region'])['Happiness Score'].mean()
# Avr scores of countries under this Region in this Year
```
4. pivot
```php
pivot_df = pd.pivot_table(data_df, index='Region', columns='Year', 
                          values=['Happiness Score', 'GDP'],
                          aggfunc='mean')                    
```
5. plot
```php
pivot_df['Happiness Score'].plot(kind='bar')
plt.show()

pivot_df['GDP'].plot(kind='bar')
plt.show()
```
