import pandas as pd 

person = {
    "first_name":["tanushree","ashwini","shristi","somya"],
    "second_name":["sinha","menon","shree","shree"],
    "email":["tnau@gmailcom","ashwini@gmail.com","shri@gmail.com","men@gmail.com"]
}

df=pd.DataFrame(person)

#Sorting on the basis of second_name [index remains same it is not like sorting me jo upar uska index 0 then index 1, nhi indexing DF bante wakt jo hui whi hogi]
# print(df.sort_values(by=["second_name"]))

#In descending order by second name
# print(df.sort_values(by=["second_name"],ascending=False))

#Sorting on the basis, jo bhi index hoga uske basis pe sort ho jayega 
# print(df.sort_index())

#Now we can place multiple column to user for sorting it will be used in prefernece when any matching happened in one other will be used 
#And in the very same way ascending True False can be given for those multiple column name

# print(df.sort_values(by=["second_name","first_name"]))
#like first df will be sort on the basis of second name if there is matching in second name, first name will be used

#Now i can pass column wise ascending descending sorting i want 
# print(df.sort_values(by=["second_name","first_name"],ascending=[True,False]))