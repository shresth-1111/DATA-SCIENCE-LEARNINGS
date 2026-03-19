import pandas as pd

# person={
#     "first_name":["tanushree","ashwini","shrishti","somya"],
#     "second_name":["sinha","menon","sharma","shree"],
#     "email":["tanushree@gmail.com","ashwini@gmail.com","shrishti@gmail.com","somya@gmail.com"]
# }

# df=pd.DataFrame(person)         #To convert a dictionary into a data frame
# print(df)

#EXTRACTION FROM DATA SETS

# print(df.email)         #To print a series or extra t a series
# print(df[["email","first_name"]])       #To extract multiple columns

# print(df.columns)       #To get detailed list of all columns

#USING iloc and loc

# print(df.iloc[0])               #To show the detail of xth row
# print(df.iloc[[0,1]])           #To show more than one row using there index number


# print(df.iloc[[0,1,2],[0,2]])           #To see the speific column detail of that row 
# You can choose multiple rows and multiple columns
# You can use [0,1,2] or can directly write 0:3 (without bradckets) df.iloc[0:3,[0,1]]

#Similarly we can use df.loc , here instead of column index we can use actual name if known

# print(df.loc[[0,1,2],["email"]])
# print(df.loc[0:4,["email","second_name"]])


