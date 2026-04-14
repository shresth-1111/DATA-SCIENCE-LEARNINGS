import pandas as pd
import numpy as np

# person={
#     "first_name":["tanushree","ashwini","shrishti","somya"],
#     "second_name":["sinha","menon","sharma","shree"],
#     "email":["tanushree@gmail.com","ashwini@gmail.com","shrishti@gmail.com","somya@gmail.com"]
# }

# df=pd.DataFrame(person)

# print(df["second_name"]=="sinha")                   #This is the filter it will give series of true and false values as per the condition

# print(df[df["second_name"]=="sinha"])               #This is to show the full details wherevr the filter has the value as true

# filt=df["second_name"]=="sinha"
# print(~filt)                                          #This is the filter it will give series of true and false values as per the condition
# print(df[~filt])                                      #This is to show the full details wherevr the filter has the value as tfalse (~ symbol is used)

#In pandas if in any column the value is NaN, the conditional operator will give any result on Nan as False without showing any error 

#Use of .str.contains()
#df["name"].str.contains(string) to check(gives true/false) this particular string lies in evry name or not 

#Use of isin 
#To check these values lies in the column or not (gives true/false)
#Can also use "or" for the same thing but this is more smarter way
# names=["somya","tanushree"]  
# print(df["first_name"].isin(names))  





