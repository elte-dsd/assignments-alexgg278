# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENtyzFEQFITo46KftiuSaBPwWcPCd7DB

# Count min-sketch

## Alejandro González
"""

import numpy as np
import math

# Request data stream
S = [str(x) for x in input('Data Stream (elements separated by sace): ').split()]

# Request error probability and error factor and calculate d and w
delta = float(input('Error probability (delta - typically: 0.1 - 0.001): '))
epsilon = float(input('Error factor (epsilon - typically: 0.5 - 0.01): '))

# Depth or number of hash functions
d = int(np.log(1/delta))

# Width
w = int(math.exp(1) / epsilon)
print(d, w0)

# Count number of unique items in the stream
N = len(np.unique(S))
elements = list(np.unique(S))
elements

# Create the hash matrix
hash_matrix = np.random.randint(w, size=(N, d))
hash_matrix

sketch = np.zeros((d, w))
sketch

for item in S:
  for h in range(d):
    sketch[h][hash_matrix[elements.index(item)][h]] += 1 
    
sketch

c = input('Frequency of: ')
l = []
for h in range(d):
  l.append(sketch[h][hash_matrix[elements.index(c)][h]])
  
count = str(int(min(l)))
print('The count of ' + c + ' in the stream is: ' + count)