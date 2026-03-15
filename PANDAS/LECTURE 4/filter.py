import pandas as pd

#SMALL PRACTICE

# person={
#     "first":['tanushree','shristi','ashwini','somya','shresth'],
#     "last":['sinha','sharma','menon','shree','sinha'],
#     "email":['tanushree.sinha@Gmail.com','shristi.sharma@gmail.com','ashwini.menon@gmail.com','somya.shree@gmail.com','shresthsinha@gmail.com']
# }

# df=pd.DataFrame(person)

# print(df)
# df.set_index('email',inplace=True)
# print(df.index)
# df.reset_index(inplace=True)
# print(df.index)
# filt=(df['last']=='sinha')
# print(df.loc[filt,'first'])

#APPLYING IT ON LARGE DATA FRAME 
# pd.set_option('display.max_column',None)

df=pd.read_csv('../survey_results_public.csv')
schema_df=pd.read_csv("../survey_results_schema.csv")

# for i in df.columns:
#     print(i)

filt=((df['CompTotal']>90000))
print(df.loc[filt,["WebframeHaveWorkedWith",'CompTotal']])