import pandas as pd

#CSV FILES

#Opening CSV files which are locally present on your system
# df=pd.read_csv("../aug_train.csv")     
# print(df)

#Opening csv from url 

#Method 1 DIRECT METHOD
# url="https://raw.githubusercontent.com/SkyTowner/sample_data/main/pandas/simple_dataset.csv"
# df=pd.read_csv(url)
# print(df)

#Method 2 HEADER METHOD  This method helpful when Creators block requests to prevent bots from overloading their servers and stealing data.
# It helps protect their performance, security, and business interests.

# import requests
# from io import StringIO

# url="https://raw.githubusercontent.com/SkyTowner/sample_data/main/pandas/simple_dataset.csv"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
# }  #This helps to show that we are actual browser sending request not a boot 

# req=requests.get(url,headers=headers) #Get text from the url
# data=StringIO(req.text) #Convert text to file format 

# df=pd.read_csv(data)  #Reads that file
# print(df)

#sep and name parameter 

#sep-to read file seprated by other charcter than comma for ex tsv files
#name-to give column heading names to all columns

#Reading tsv without sep and name
# df=pd.read_csv("../movie_titles_metadata.tsv")
# print(df)

#Reading tsv with sep
# df2=pd.read_csv("../movie_titles_metadata.tsv",sep="\t")
# print(df2)

#Giving column names
# df3=pd.read_csv("../movie_titles_metadata.tsv",sep="\t",names=["sno","movie_name","year","rating","tickets_Sold","genre"])
# print(df3)

#Header Parameter

#Without header
# df=pd.read_csv("../test.csv")
# print(df)

#With header
# df2=pd.read_csv("../test.csv",header=1)
# print(df2)

#Uisng usecols
# df=pd.read_csv("../aug_train.csv",usecols=["enrollee_id","gender","education_level"])
# print(df)

#Using skip rows

#Without function
# df=pd.read_csv("../aug_train.csv",skiprows=[1])
# print(df)

#With function
# def select_row(val):
#     if val==0:
#         return False
#     if val%5!=0:
#         return True
    
# df=pd.read_csv("../aug_train.csv",skiprows=select_row)
# print(df)

#Using encoding

#Without encoding
# df=pd.read_csv("../zomato.csv")
# print(df)  #Giving Error

#With encoding
# df=pd.read_csv("../zomato.csv",encoding="latin-1")
# print(df)  #Will open this time

#With skipbadlines
# df=pd.read_csv("../BX-Books.csv",encoding="latin-1",error_bad_lines=False)
# print(df)    

#Without Converters
# df=pd.read_csv("../IPL Matches 2008-2020.csv")
# print(df.team1)

#With converters
# def rename_team(team_name):
#     if (team_name=="Royal Challengers Bangalore"):
#         return "RCB"
#     else:
#         return team_name

# df=pd.read_csv("../IPL Matches 2008-2020.csv",converters={"team1":rename_team,"team2":rename_team})
# print(df.team1)
# print(df.team2)


#EXCEL SHEETS 

# df=pd.read_excel("excel file address")
# print(df)   #This will print the first sheet of the file 

#For printing other sheets of the file
# df=pd.read_csv("excel file address",sheet_name="excel sheet name of that file")
# print(df)


#JSON DATA

#USING FILE
# df=pd.read_json("../train.json")
# print(df)

#USING URL
# df2=pd.read_csv(#Write the link here)
# print(df2)


#SQL DATA

# import mysql.connector

# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="****",
#     database="world"
# )

# df=pd.read_sql_query("SELECT * FROM city",conn)
# print(df)

# df2=pd.read_sql_query("SELECT * FROM city WHERE CountryCode = 'IND'",conn)
# print(df2)


