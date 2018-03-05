import numpy as np
from numpy import array
#1d array
print(array([1,2,3,4]))
#2d array
arr=array([[1,2,3,4],['sajan','ram','hari','shyam']])
print(arr)
#accessing a particular row and column frm 2d array
value=arr[1,:1] #array[row,: colum] : is for slicing
print(value)
print(type(value))
print(arr.shape)
