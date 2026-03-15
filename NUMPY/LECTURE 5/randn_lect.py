import numpy as np

#USING randn()

#1-D randn()
ar1=np.random.randn(4)
print(ar1)
print(ar1.ndim)

#2-D randn()
ar2=np.random.randn(2,4)
print(ar2)
print(ar2.ndim)

#3-D randn()
ar3=np.random.randn(2,2,6)
print(ar3)
print(ar3.ndim)