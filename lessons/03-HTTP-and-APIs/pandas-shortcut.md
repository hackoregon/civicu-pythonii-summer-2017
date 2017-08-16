

```python
import csv


# writer example 
with open('grid.csv', 'w') as fout:
    foo_writer = csv.writer(foo)
    foo_writer.writerow("A B C D".split())
    for i in range(10):
        foo_writer.writerow("A{i} B{i} C{i} D{i}".format(i=i).split()))

filename = 'food-carbon-footprint.csv'
# reader example
with open('grid.csv') as fin: 
    reader = csv.reader(fin)
    
    # this is how you can grab the first header row out of a csv
    header_row = next(reader)
    
    for row in foo_reader:
        print(row)
   
    

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-2-44d1ad2e1a1a> in <module>()
          2 
          3 # reader example
    ----> 4 with open("foo.csv") as foo:
          5     foo_reader = csv.reader(foo)
          6 


    FileNotFoundError: [Errno 2] No such file or directory: 'foo.csv'



```python

```


```python
import pandas as pd
df = pd.read_html('http://www.greeneatz.com/foods-carbon-footprint.html', header=0)[0]
df.to_csv('food-carbon-footprint.csv')
df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Food</th>
      <th>CO2 Kilos Equivalent</th>
      <th>Car Miles Equivalent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Lamb</td>
      <td>39.2</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Beef</td>
      <td>27.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Cheese</td>
      <td>13.5</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Pork</td>
      <td>12.1</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Turkey</td>
      <td>10.9</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Chicken</td>
      <td>6.9</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Tuna</td>
      <td>6.1</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Eggs</td>
      <td>4.8</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Potatoes</td>
      <td>2.9</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Rice</td>
      <td>2.7</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Nuts</td>
      <td>2.3</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Beans/tofu</td>
      <td>2.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Vegetables</td>
      <td>2.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Milk</td>
      <td>1.9</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Fruit</td>
      <td>1.1</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Lentils</td>
      <td>0.9</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
df.mean()
for i, row in df.iterrows():
    print(row)
```

    Rank                       1
    Food                    Lamb
    CO2 Kilos Equivalent    39.2
    Car Miles Equivalent      91
    Name: 0, dtype: object
    Rank                       2
    Food                    Beef
    CO2 Kilos Equivalent      27
    Car Miles Equivalent      63
    Name: 1, dtype: object
    Rank                         3
    Food                    Cheese
    CO2 Kilos Equivalent      13.5
    Car Miles Equivalent        31
    Name: 2, dtype: object
    Rank                       4
    Food                    Pork
    CO2 Kilos Equivalent    12.1
    Car Miles Equivalent      28
    Name: 3, dtype: object
    Rank                         5
    Food                    Turkey
    CO2 Kilos Equivalent      10.9
    Car Miles Equivalent        25
    Name: 4, dtype: object
    Rank                          6
    Food                    Chicken
    CO2 Kilos Equivalent        6.9
    Car Miles Equivalent         16
    Name: 5, dtype: object
    Rank                       7
    Food                    Tuna
    CO2 Kilos Equivalent     6.1
    Car Miles Equivalent      14
    Name: 6, dtype: object
    Rank                       8
    Food                    Eggs
    CO2 Kilos Equivalent     4.8
    Car Miles Equivalent      11
    Name: 7, dtype: object
    Rank                           9
    Food                    Potatoes
    CO2 Kilos Equivalent         2.9
    Car Miles Equivalent           7
    Name: 8, dtype: object
    Rank                      10
    Food                    Rice
    CO2 Kilos Equivalent     2.7
    Car Miles Equivalent       6
    Name: 9, dtype: object
    Rank                      11
    Food                    Nuts
    CO2 Kilos Equivalent     2.3
    Car Miles Equivalent       5
    Name: 10, dtype: object
    Rank                            12
    Food                    Beans/tofu
    CO2 Kilos Equivalent             2
    Car Miles Equivalent           4.5
    Name: 11, dtype: object
    Rank                            13
    Food                    Vegetables
    CO2 Kilos Equivalent             2
    Car Miles Equivalent           4.5
    Name: 12, dtype: object
    Rank                      14
    Food                    Milk
    CO2 Kilos Equivalent     1.9
    Car Miles Equivalent       4
    Name: 13, dtype: object
    Rank                       15
    Food                    Fruit
    CO2 Kilos Equivalent      1.1
    Car Miles Equivalent      2.5
    Name: 14, dtype: object
    Rank                         16
    Food                    Lentils
    CO2 Kilos Equivalent        0.9
    Car Miles Equivalent          2
    Name: 15, dtype: object



```python

```


```python

```


```python

```


```python

```
