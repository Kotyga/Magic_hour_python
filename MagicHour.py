# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10jCO44QkEnRwdUrRvgAVmkJ1qvj9kDaN
"""

h = [i for i in range(24)]

count = 0
summ = 0

for hour in h:
  if h[hour] < 10:
    if  int(str(h[hour]) + '0') < 60:
      summ += abs(int('0' + str(h[hour])) - int(str(h[hour]) + '0'))
      count += 1
      #print(abs(int('0' + str(h[hour])) - int(str(h[hour]) + '0')))
  if h[hour] >= 10:
    if  int(int(str(h[hour])[1] + str(h[hour])[0])) < 60:
      summ += abs(int(str(h[hour])[0] + str(h[hour])[1]) - int(str(h[hour])[1] + str(h[hour])[0]))
      count += 1
      #print(abs(int(str(h[hour])[0] + str(h[hour])[1]) - int(str(h[hour])[1] + str(h[hour])[0])))
#print(summ)
#print(count)
print(summ/count)