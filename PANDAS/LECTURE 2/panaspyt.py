import pandas as pd

# df=pd.read_csv("../survey_results_public.csv")
# print(df)

person={
    "first":['tanushree','shristi','ashwini','somya'],
    "last":['sinha','sharma','menon','shree'],
    "email":['tanushree.sinha@Gmail.com','shristi.sharma@gmail.com','ashwini.menon@gmail.com','somya.shree@gmail.com']
}

df=pd.DataFrame(person)
# print(df)

# print(df['email'])

# print(df[["email","last"]])

# print(df.columns)

# print(df.iloc[[1,0,2]])


# print(df.iloc[0:2])

# print(df.iloc[0:2,0:3])
