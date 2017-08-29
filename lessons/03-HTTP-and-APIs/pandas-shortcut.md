

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


      File "<ipython-input-2-71ed9379c21b>", line 9
        foo_writer.writerow("A{i} B{i} C{i} D{i}".format(i=i).split()))
                                                                      ^
    SyntaxError: invalid syntax




```python

```


```python
import pandas as pd
df = pd.read_html('http://www.greeneatz.com/foods-carbon-footprint.html', header=0)[0]
df.to_csv('food-carbon-footprint.csv')
df

```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-3-4d9dc66c38ab> in <module>()
          1 import pandas as pd
    ----> 2 df = pd.read_html('http://www.greeneatz.com/foods-carbon-footprint.html', header=0)[0]
          3 df.to_csv('food-carbon-footprint.csv')
          4 df


    C:\Users\Dennis\Anaconda3-64\lib\site-packages\pandas\io\html.py in read_html(io, match, flavor, header, index_col, skiprows, attrs, parse_dates, tupleize_cols, thousands, encoding)
        872     _validate_header_arg(header)
        873     return _parse(flavor, io, match, header, index_col, skiprows,
    --> 874                   parse_dates, tupleize_cols, thousands, attrs, encoding)
    

    C:\Users\Dennis\Anaconda3-64\lib\site-packages\pandas\io\html.py in _parse(flavor, io, match, header, index_col, skiprows, parse_dates, tupleize_cols, thousands, attrs, encoding)
        724     retained = None
        725     for flav in flavor:
    --> 726         parser = _parser_dispatch(flav)
        727         p = parser(io, compiled_match, attrs, encoding)
        728 


    C:\Users\Dennis\Anaconda3-64\lib\site-packages\pandas\io\html.py in _parser_dispatch(flavor)
        668     if flavor in ('bs4', 'html5lib'):
        669         if not _HAS_HTML5LIB:
    --> 670             raise ImportError("html5lib not found, please install it")
        671         if not _HAS_BS4:
        672             raise ImportError(


    ImportError: html5lib not found, please install it



```python

```


```python
df.mean()
for i, row in df.iterrows():
    print(row)
    print('/n')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-2f743d0c0ab7> in <module>()
    ----> 1 df.mean()
          2 for i, row in df.iterrows():
          3     print(row)
          4     print('/n')


    NameError: name 'df' is not defined



```python

```


```python

```


```python

```


```python

```
