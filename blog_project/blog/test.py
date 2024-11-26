import pandas as pd
from sqlalchemy  import create_engine

engine = create_engine("postgresql://hints:hints@40.90.194.2:5432/hints")

con = engine.connect()

df = pd.read_sql("select * from dbo.tabvolunteers order by volunteerid asc limit 22", con=con)

df_1 = pd.read_sql("select * from dbo.tabdevoteeinfo order by username desc limit 22", con=con)

df['username'] = df_1['username']

df["activityid"] = 2

df.drop(columns = "volunteerid", axis=1, inplace=True)

print(len(df))

print(df)
df.to_sql('tabvolunteers',con = con, index=False, schema="dbo", if_exists="append")


con.commit()
con.close()
print("Done")


