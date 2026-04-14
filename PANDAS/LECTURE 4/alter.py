import pandas as pd

person={
    "first_name":["tanushree","ashwini","shrishti","somya"],
    "second_name":["sinha","menon","sharma","shree"],
    "email":["tanushree@gmail.com","ashwini@gmail.com","shrishti@gmail.com","somya@gmail.com"]
}

df=pd.DataFrame(person)

#There are various method to change column name 

#Method 1 : Changing the name of all columns
# print(df.columns)
# df.columns=["first","second","email_info"]   #This will change the column names you donot need to do inplace=True
# print(df.columns)                            #Will show new columns name 

#Method 2 : Using fucntion and applying all at once 
#For Ex : Changing the case to uppercase

# df.columns=[x.upper()  for x in df.columns]  # Upper Case me convert karke new value assign kar di
# print(df.columns)

#Method 3 : Using str.replace("old","new") to replace a particular part in column name 
# print(df.columns)

#Let us replace  _  with  " "
# df.columns=df.columns.str.replace("_"," ")
# print(df.columns)

#Method 4 : Changing specific columns name (We will do this using df.rename)
# print(df.columns)

# df.rename(columns={
#     "first_name" : "first",
#     "second_name":"second"
# },inplace=True)

# print(df.columns)

#How to change row 

#Method 1 : Changing full row

# print(df.iloc[[2]])
# df.iloc[2]=["shrishti","shree","shristi@gmail.com"] #Chnaging all the details of row with index 2
# print(df.iloc[[2]])

#Method 2 : Changing specific info of a row
#   





