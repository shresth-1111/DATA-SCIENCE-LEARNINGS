import numpy as np

#FULL ARRAY

#1-D FULL ARRAY
# ar1=np.full((4),3)
# print(ar1)
# print(ar1.ndim)

#2-D FULL ARRAY
# ar2=np.full((3,5),3.14)
# print(ar2)
# print(ar2.ndim)

#3-D FULL ARRAY
# ar3=np.full((3,5,2),"Tanushree")
# print(ar3)
# print(ar3.ndim)


#DIAGONAL ARRAY

#2-D DIAGONAL ARRAY
# ar1=np.eye(5)
# print(ar1)
# print(ar1.ndim)

# ar1=np.eye(2,5,3)
# print(ar1)
# print(ar1.ndim)

#ARANGE WITH VARIATIONS 
# ar1=np.arange(4,11,4)
# print(ar1)
# print(ar1.ndim)

#RANDOM IN NUMPY

#USING RANDOM.RANDOM

#1-D RANDOM
# ar1=np.random.random(5)
# print(ar1)
# print(ar1.ndim)

#2-D RANDOM
# ar2=np.random.random((5,5))
# print(ar2)
# print(ar2.ndim)

#3-D RANDOM
# ar3=np.random.random((2,5,3))
# print(ar3)
# print(ar3.ndim)

#USING RANDOM.RANDINT

#1-D RANDINT
# ar1=np.random.randint(4,11,(3))
# print(ar1)
# print(ar1.ndim)

# 2-D RANDINT
# ar2=np.random.randint(4,14,(3,5))
# print(ar2)
# print(ar2.ndim)

#3-D RANDINT
# ar3=np.random.randint(4,5,(3,3,3))
# print(ar3)
# print(ar3.ndim)