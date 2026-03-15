import numpy as np

#SEARCH IN A NUMPY ARRAY

#1-D ARRAYS
# var=np.array([1,2,3,4,5,6,7])
# idx=np.where(var==2)
# print(idx)

#2-D ARRAYS
# var=np.array([[1,2,3],[4,5,6]])
# idx=np.where(var==3)
# print(idx)

#3-D ARRAYS
# var=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# idx=np.where(var==5)
# print(idx)

#SEARCH THE POSITION TO INSERT INSIDE A SORTED ARRAY 

#1-D ARRAY
# var=np.array([1,2,3,4,5,6,"Shresth"])
# idx=np.searchsorted(var,"Shresth")      //For strings it will compare alphabets one by one shorter one will be placed first
# idx2=np.searchsorted(var,"Sbnha")
# print(idx)

#THIS IS NOT DIRECTLY APPLICABLE FOR 2-D AND 3-D ARRAYS 

#SORT ARRAY

#1-D ARRAY
# var=np.array([1,5,64,8,6,5,3,2,5,46,5,8,6,9,69,3])
# print(np.sort(var))

#2-D ARRAY[AXIS=0]
# var=np.array([[6,2,4],[1,5,10]])
# print(np.sort(var,axis=0))

#2-D ARRAY[AXIS=1]
