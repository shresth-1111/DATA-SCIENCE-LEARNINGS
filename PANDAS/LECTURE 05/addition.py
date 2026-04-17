import pandas as pd 

person={
    "first_name":["tanushree","ashwini","somya"],
    "last_name":["sinha","menon","shree"],
    "email":["tanu@gmail.com","ash@gmail.com","som@gmail.com"]
} 

df=pd.DataFrame(person)


#Additon of new columns inside the data frame

# print(df)

#Making full_name which is the sum of first and last
# df["full_name"]=df["first_name"]+" "+df["last_name"]

# print(df)

#Deletion of columns 
#To make the deletion permanent use inplace=True

# print(df)

# df.drop(columns=["first_name","last_name"],inplace=True)

# print(df)

#Now Be very careful while using drop option you can bring back those columns if you have something present in data otherwise not possible
#Like first_name and last_name can be extracted from full_name 

# df[["first_name","last_name"]]=df["full_name"].str.split(" ",expand=True)

# print(df)


#Additon of new row inside the data frame
#Additon is always done on the last  

# df.loc[len(df)]={
#     "first_name":"Shresth",
#     "last_name":"Sinha",
#     "email":"shr@gmail.com"
# }

# print(df)

#Deletion of rows 

#Method 1 using index of the row 

# print(df)
# df.drop(index=1,inplace=True)
# print(df)

#Method 2 using condition/filter
# print(df)
# df.drop(index=df[df["first_name"]=="tnaushree"].index,inplace=True)
# print(df)


