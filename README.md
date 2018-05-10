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
  - ascending: ↑, low-high
  - year: low-high, 2013-2014-2015  
  - score: high-low

3. groupby - MULTI COLUMNS - MULTI-IDNEX
```php
grouped_year_region_df = data_df.groupby(by=['Year','Region'])['Happiness Score'].mean()
# Avr scores of countries under this Region in this Year
```
```
Year  Region                         
2015  Australia and New Zealand          7.285000
      Central and Eastern Europe         5.332931
      Eastern Asia                       5.626167
      Latin America and Caribbean        6.144682
      Middle East and Northern Africa    5.406900
      North America                      7.273000
      Southeastern Asia                  5.317444
      Southern Asia                      4.580857
      Sub-Saharan Africa                 4.202800
      Western Europe                     6.689619
2016  Australia and New Zealand          7.323500
      Central and Eastern Europe         5.370690
      Eastern Asia                       5.624167
      Latin America and Caribbean        6.101750
      Middle East and Northern Africa    5.386053
      North America                      7.254000
      Southeastern Asia                  5.338889
      Southern Asia                      4.563286
      Sub-Saharan Africa                 4.136421
      Western Europe                     6.685667
2017  Australia and New Zealand          7.299000
      Central and Eastern Europe         5.409931
      Eastern Asia                       5.646667
      Latin America and Caribbean        5.957818
      Middle East and Northern Africa    5.369684
      North America                      7.154500
      Southeastern Asia                  5.444875
      Southern Asia                      4.628429
      Sub-Saharan Africa                 4.111949
      Western Europe                     6.703714
Name: Happiness Score, dtype: float64

```


4. pivot
```php
pivot_df = pd.pivot_table(data_df, index='Region', columns='Year', 
                          values=['Happiness Score', 'GDP'],
                          aggfunc='mean')                    
```

```
                                Economy (GDP per Capita)                      \
Year                                                2015      2016      2017   
Region                                                                         
Australia and New Zealand                       1.291880  1.402545  1.445060   
Central and Eastern Europe                      0.942438  1.047537  1.092051   
Eastern Asia                                    1.151780  1.277312  1.318716   
Latin America and Caribbean                     0.876815  0.993410  1.006981   
Middle East and Northern Africa                 1.066973  1.139323  1.168535   
North America                                   1.360400  1.474055  1.512732   
Southeastern Asia                               0.789054  0.896381  0.965253   
Southern Asia                                   0.560486  0.660671  0.697479   
Sub-Saharan Africa                              0.380473  0.474321  0.501749   
Western Europe                                  1.298596  1.417056  1.457411   
                                Happiness Score                      
Year                                       2015      2016      2017  
Region                                                               
Australia and New Zealand              7.285000  7.323500  7.299000  
Central and Eastern Europe             5.332931  5.370690  5.409931  
Eastern Asia                           5.626167  5.624167  5.646667  
Latin America and Caribbean            6.144682  6.101750  5.957818  
Middle East and Northern Africa        5.406900  5.386053  5.369684  
North America                          7.273000  7.254000  7.154500  
Southeastern Asia                      5.317444  5.338889  5.444875  
Southern Asia                          4.580857  4.563286  4.628429  
Sub-Saharan Africa                     4.202800  4.136421  4.111949  
Western Europe                         6.689619  6.685667  6.703714  

```

5. plot
```php
pivot_df['Happiness Score'].plot(kind='bar')
plt.show()

pivot_df['GDP'].plot(kind='bar')
plt.show()
```
