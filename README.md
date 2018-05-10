# Happiness Report Analyse

# 0 
1. Read csv data
```php
data_df.read_csv('./csv')
```
2. Sort values
```php
data_df.sort_values(['Year','Score'], ascending=[True, False], inplace=True)
```
3. Rank / Classify 1
```php
def func():
    ... ...

data_df['new_col'] = data_df['Score'].apply(func)
```
4. Rank / Classify 2
```php
data_df['new_col'] = pd.cut(data_df['Score'],bins=[-np.inf,3,5,np.inf],labels=['a','b','c'])
```
5. Pivot table
```php
pivot_df = pd.pivot_table(data_df, index='Region', columns=['Year','Level'],
                            values=['Country'], aggfunc='count')
```
6. Stacked bar plot
```php
pivot_df['values', 'columns'].plot(kind='bar', stacked=True, rot=0, title='plot')
plt.show()
```


# 1. Happiness Score
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

```
         Country                     Region  Happiness Rank  Happiness Score  \
141  Switzerland             Western Europe             1.0            7.587   
60       Iceland             Western Europe             2.0            7.561   
38       Denmark             Western Europe             3.0            7.527   
108       Norway             Western Europe             4.0            7.522   
25        Canada              North America             5.0            7.427   
46       Finland             Western Europe             6.0            7.406   
102  Netherlands             Western Europe             7.0            7.378   
140       Sweden             Western Europe             8.0            7.364   
103  New Zealand  Australia and New Zealand             9.0            7.286   
6      Australia  Australia and New Zealand            10.0            7.284   
     Economy (GDP per Capita)  Year  
141                   1.39651  2015  
60                    1.30232  2015  
38                    1.32548  2015  
108                   1.45900  2015  
25                    1.32629  2015  
46                    1.29025  2015  
102                   1.32944  2015  
140                   1.33171  2015  
103                   1.25018  2015  
6                     1.33358  2015  

```


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
![](https://github.com/davidkorea/happiness_score/blob/master/pivot_score.png)
![](https://github.com/davidkorea/happiness_score/blob/master/pivot_gdp.png)


# 2. Hapiness Level
## 2.1 Basic
![](https://github.com/davidkorea/happiness_score/blob/master/images/task2.jpg)
![](https://github.com/davidkorea/happiness_score/blob/master/images/apply.jpg)
![](https://github.com/davidkorea/happiness_score/blob/master/images/cut.jpg)

## 2.2 Summary
1. collect_data()
```php
data_df = pd.read_csv('./data_pd/csv')
data_df.dropna(inplace=True)
```
2. sort_data
```php
data_df.sort_values(['Year','Happiness Score'],ascending=[True,False].inplaxe=True)
```
3. create Level 
create a new column named 'Level', which is ranked by 'Scores'
- apply()
```php
def score2level(vars):
    if var <= 3:
        level = 'Low'
    elif var <= 5:
        level = 'Middle'
    else:
        level = 'High'
    return level

data_df['Level'] = data_df['Happiness Score'].apply(score2level)
```
- cut() 连续性的数值分组/切分
```php
import numpy as np
# -∞ = -np.inf, +∞ = np.inf
data_df['Level'] = pd.cut(data_df['Happiness Score'], bins=[-np.inf,3,5,np.inf], labels=['Low','Middle','High'])
```
4. pivot
```php
pivot_df = pd.pivot_table(data_df, index='Region', columns=['Year','Level'],
                            values=['Country'], aggfunc='count')
pivot_df.fillna(0,inplace=True)
```

```
                                Country                                      \
Year                               2015              2016              2017   
Level                               Low Middle  High  Low Middle  High  Low   
Region                                                                        
Australia and New Zealand           NaN    NaN   2.0  NaN    NaN   2.0  NaN   
Central and Eastern Europe          NaN    8.0  21.0  NaN    6.0  23.0  NaN   
Eastern Asia                        NaN    1.0   5.0  NaN    1.0   5.0  NaN   
Latin America and Caribbean         NaN    3.0  19.0  NaN    2.0  22.0  NaN   
Middle East and Northern Africa     NaN    8.0  12.0  NaN    6.0  13.0  NaN   
North America                       NaN    NaN   2.0  NaN    NaN   2.0  NaN   
Southeastern Asia                   NaN    3.0   6.0  NaN    3.0   6.0  NaN   
Southern Asia                       NaN    5.0   2.0  NaN    5.0   2.0  NaN   
Sub-Saharan Africa                  2.0   34.0   4.0  1.0   34.0   3.0  2.0   
Western Europe                      NaN    1.0  20.0  NaN    NaN  21.0  NaN   
                                              
Year                                          
Level                           Middle  High  
Region                                        
Australia and New Zealand          NaN   2.0  
Central and Eastern Europe         5.0  24.0  
Eastern Asia                       1.0   5.0  
Latin America and Caribbean        1.0  21.0  
Middle East and Northern Africa    7.0  12.0  
North America                      NaN   2.0  
Southeastern Asia                  2.0   6.0  
Southern Asia                      5.0   2.0  
Sub-Saharan Africa                34.0   3.0  
Western Europe                     NaN  21.0 
```

```
                                Country                                      \
Year                               2015              2016              2017   
Level                               Low Middle  High  Low Middle  High  Low   
Region                                                                        
Australia and New Zealand           0.0    0.0   2.0  0.0    0.0   2.0  0.0   
Central and Eastern Europe          0.0    8.0  21.0  0.0    6.0  23.0  0.0   
Eastern Asia                        0.0    1.0   5.0  0.0    1.0   5.0  0.0   
Latin America and Caribbean         0.0    3.0  19.0  0.0    2.0  22.0  0.0   
Middle East and Northern Africa     0.0    8.0  12.0  0.0    6.0  13.0  0.0   
North America                       0.0    0.0   2.0  0.0    0.0   2.0  0.0   
Southeastern Asia                   0.0    3.0   6.0  0.0    3.0   6.0  0.0   
Southern Asia                       0.0    5.0   2.0  0.0    5.0   2.0  0.0   
Sub-Saharan Africa                  2.0   34.0   4.0  1.0   34.0   3.0  2.0   
Western Europe                      0.0    1.0  20.0  0.0    0.0  21.0  0.0   
                                              
Year                                          
Level                           Middle  High  
Region                                        
Australia and New Zealand          0.0   2.0  
Central and Eastern Europe         5.0  24.0  
Eastern Asia                       1.0   5.0  
Latin America and Caribbean        1.0  21.0  
Middle East and Northern Africa    7.0  12.0  
North America                      0.0   2.0  
Southeastern Asia                  2.0   6.0  
Southern Asia                      5.0   2.0  
Sub-Saharan Africa                34.0   3.0  
Western Europe                     0.0  21.0  
```
5. plot
```php
# pivot_df['Country',2015].plot(kind='bar',stacked=True)
for year in [2015,2016,2017]:
    pivot_df['Country', year].plot(bind='bar', stacked=True)
    plt.show()
```
