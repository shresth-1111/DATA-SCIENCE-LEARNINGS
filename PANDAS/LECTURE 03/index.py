import pandas as pd

person={
    "first_name":["tanushree","ashwini","shrishti","somya"],
    "second_name":["sinha","menon","sharma","shree"],
    "email":["tanushree@gmail.com","ashwini@gmail.com","shrishti@gmail.com","somya@gmail.com"]
}

df=pd.DataFrame(person)
# print(df.index)  #This is the bydefault indexing 0,1,2---

# df.set_index("email")         #We chganged the index to email 
# print(df.first_name)          #Still not permanently changed

# df.set_index("email",inplace=True)  #Now here the change is permanent
# print(df.first_name)

# df.reset_index(inplace=True)        #Resetting to default, it CREATES A NEW COLUMN INDEX WITH OLDER NUMBERS 
# print(df.first_name)

#inplace=True is VERY VERY IMPORTANT

#ANOTHER WAY OF DECIDING THE INDEX
# df=pd.read_csv(-----,index_col="whatever column u want as index")

#SORTING ON THE BASIS OF INDEXING
# print(df.sort_index(ascending=False))
