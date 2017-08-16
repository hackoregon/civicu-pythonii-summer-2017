

```python
import os
# !pip install seaborn
import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# !pip install mpld3
import mpld3
import json

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 10)
%matplotlib inline
mpld3.enable_notebook()
```


```python
# Let's talk about dict and zip
dict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)])
```




    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}




```python
# zip can create that pairing for us by zippering up two sides (lists) together
zipped = zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4])
print(zipped)
```

    <zip object at 0x7f76bc74c188>



```python

```


```python
# dict will accept any sequences of pairings (2-tuples)
# but what if we have two sequences of values that we want to "pair up"
# zip brings the two sides of a pair (the sides of a zipper) together in an alligned pairing
list(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))
```




    [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]




```python
# and a dict is can take a list of pairs, like before... so
dict(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))
```




    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}




```python
# and `range(5)` is a sequence (iterable)
dict(zip(['a', 'b', 'c', 'd', 'e'], range(5)))
```




    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}




```python
# if we get the length wrong, the zipper will get "stuck" on the shortest sequence
dict(zip(['a', 'b', 'c', 'd', 'e'], range(4)))
```




    {'a': 0, 'b': 1, 'c': 2, 'd': 3}




```python
# or because any sequence will do, and a str is a sequence of characters:
dict(zip('abcde', range(5)))
```




    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}




```python
# What will happen if you try to coerce a list of 3-tuples into a dict?
dict([('a', 1, 2), ('b', 3, 4)])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-29-f7adccc027f6> in <module>()
          1 # What will happen if you try to coerce a list of 3-tuples into a dict?
    ----> 2 dict([('a', 1, 2), ('b', 3, 4)])
    

    ValueError: dictionary update sequence element #0 has length 3; 2 is required



```python
x = list(range(3))
y = list(range(4))
print(x)
print(y)
list(zip(x, y, range(5)))

```

    [0, 1, 2]
    [0, 1, 2, 3]





    [(0, 0, 0), (1, 1, 1), (2, 2, 2)]




```python
x = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
list(zip(*x))

```




    [(0, 1, 2), (0, 1, 2), (0, 1, 2)]




```python
list(zip(x[0], x[1], x[2]))
```




    [(0, 1, 2), (0, 1, 2), (0, 1, 2)]


