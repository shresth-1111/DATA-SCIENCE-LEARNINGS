import numpy as np

# np.add(), np.subtract(), np.multiply() etc. perform element-wise arithmetic operations 
# between arrays and do not change the array’s dimensions.

# Reduction functions like np.sum(), np.mean(), np.max() operate within a single array 
# and can reduce dimensions by performing operations along a specified axis.

#USING np.sum()

#1-D
# arr1=np.array([15,20,25,30])
# print(np.sum(arr1,axis=0))

#2-D
# arr2=np.array([[1,2],[3,4]])
# print(np.sum(arr2,axis=0))
# print(np.sum(arr2,axis=1))

#3-D
# arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(np.sum(arr3,axis=0))
# print(np.sum(arr3,axis=1))
# print(np.sum(arr3,axis=2))

#For keeping the dimension as it is (not talking about shape) use keepdims=True

#Similarly you can do np.min(), np.max(), np.max(), np.argmin(), np.argmax()

#np.argmin()  - tells us the index position of the minimum one 

#1-D
# arr1=np.array([15,2,100,3,56])
# print(np.argmin(arr1))

#2-D
# arr2=np.array([[1,21,3],[4,2,6]])
# print(np.argmin(arr2,axis=0))
# print(np.argmin(arr2,axis=1))

#3-D
# arr3=np.array([[[15,50,30],[40,23,36]],[[52,32,12],[42,63,27]]])
# print(np.argmin(arr3,axis=0))
# print(np.argmin(arr3,axis=1))
# print(np.argmin(arr3,axis=2))



#Now some other function where shape and dimension donot changes 
#These are np.sin(), np.cos(), np.sqrt()

#np.sqrt()

#1-D
# arr1=np.array([64,16,9])
# print(np.sqrt(arr1))

#2-D
# arr2=np.array([[25,225,169],[64,49,36]])
# print(np.sqrt(arr2))

#3-D
# arr3=np.array([[[64,225,400],[169,196,729]],[[625,900,1600],[25,16,4]]])
# print(np.sqrt(arr3))


#Now few other functions are np.cumsum(), np.cumprod()
#Axis effect is there but there is no dimension change in this(if axis not given it treat any dimesion array as 1-d) 

# cum here - stands for cummulative

#1-D
# arr1=np.array([15,26,30,45])
# print(np.cumsum(arr1))

#2-D
# arr2=np.array([[10,12,30],[8,6,1]])
# print(np.cumsum(arr2,axis=0))
# print(np.cumsum(arr2,axis=1))

#3-D
# arr3=np.array([[[15,20,8],[6,30,41]],[[54,32,62],[12,32,17]]])
# print(np.cumsum(arr3,axis=0))
# print()
# print(np.cumsum(arr3,axis=1))
# print()
# print(np.cumsum(arr3,axis=2))


