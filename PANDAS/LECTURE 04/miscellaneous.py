import pandas as pd 

person={
    "first_name":["tanushree","ashwini","shristi","somya"],
    "second_name":["sinha","menon","shree","shree"],
    "email":["tanu#gmail.com","ashwini@gmail.com","shristi@gmail.com","somya@gmail.com"]
}

df=pd.DataFrame(person)

#APPLY : USED TO APPLY SOMETHING ON THE WHOLE COLUMN OR ROW 

# print(df["email"].apply(len))
#Here, len is an built in function, it will give the length of email in whole column

#I can also use my user built fucntion 
# def update_email(email):
#     return email.upper()

# print(df["email"].apply(update_email))
#To mkae the above change permanent just do df["email"]=df["email"].apply(update_email)

#APPLYING ON WHOLE DATAFRAME 

# print(df.apply(len))
#It will give the count of evry column 
#Bascially how many data is there in that column 

#Now if you want to count number of columns in each row (har row ki kitni details hai hamare pass) 
# print(df.apply(len,axis="columns"))


#MAP : Used to change all the data of the column series with new value 
#The one we donot change turns into NaN

# print(df["first_name"])

#To store the changes 
# df["first_name"]=df["first_name"].map({
#     "tanushree":"i am she",
#     "ashwini":"i am two she",
#     //This will change into Nan as we not mapped any change for "shristi"
#     "somya":"I am four she"
# })S

# print(df["first_name"])

#Now to avoid this issue of NaN we use replace instead of map 
#Replace allow us to change only those columns details which we want

# print(df["first_name"])

# #To store the changes
# df["first_name"]=df["first_name"].replace({
#     "tanushree":"tanu",
#     "somya":"gullu"
# })

#Here shristi and ashwini will not change into Nan

# print(df["first_name"])






