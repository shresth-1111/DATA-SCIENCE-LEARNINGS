import numpy as np

#ADDITION OF TWO ARRAYS
# arr1=np.array([6,7,9,27])
# arr2=np.array([25,18,11,11])
# add1=np.add(arr1,arr2)
# add2=arr1+arr2
# print(add1)
# print(add2)

#ADDITION OF ONE ARRAY AND ONE NUMBER 
# arr=np.array([10,11,12,13])
# add=arr+3  #3 will broadcast itself to a shape same to that of arr i.e. (4,)
# print(add)

#SIMILARLY YOU CAN PERFORM MULTIPLICATION,DIVISION,SUBTRACTION,MOD,POWER,RECIPROCAL

#CONCEPT OF BROADCASTING

#Question1
# arr1=np.array([[1],[2],[3]])
# arr2=np.array([10,20,30])
# print(arr1.shape)
# print(arr2.shape)
# res=arr1+arr2
# print(res)
# print(res.shape)

#Question2
# arr1 = np.array([[1,2,3]])
# arr2 = np.array([[10],[20],[30]])
# print(arr1.shape)
# print(arr2.shape)
# res=arr1+arr2
# print(res)
# print(res.shape)

#Quesiton3
# arr = np.array([[1,2],[3,4]])
# print(arr.shape)
# res=arr*5
# print(res)
# print(res.shape)

#Question4
# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([10,20])
# print(arr1.shape)   #(2,3)
# print(arr2.shape)   #(2,)
# try:
#     res=arr1+arr2
#     print(res)
#     print(res.shape)
# except:
#     print("BRODCASTING FAILURE")

#It will fail as (2,3) and( ,2) comparing 3 and 2 neither same nor any one of them is 1.
 
#Question5
# arr1 = np.array([[[1,2,3]]])
# arr2 = np.array([10,20,30])
# print(arr1.shape)
# print(arr2.shape)
# res=arr1+arr2
# print(res)
# print(res.shape)



# VERY VERY IMPORTANT

# Arithmetic operators (+ - * /) perform element-wise operations with broadcasting and do not use axis.

# axis parameter is used in reduction functions like np.sum(), np.mean(), np.max() to specify the dimension along which the operation is performed.

# Element-wise operations operate on corresponding elements of arrays, while axis-based operations combine values along rows or columns.