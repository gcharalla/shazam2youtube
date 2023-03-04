import pandas as pd

df = pd.read_csv('shazamlibrary.csv', skiprows=1)

df["URL"] = df["Title"].str.cat(df["Artist"], sep="+")

df["URL"] = df["URL"].replace(" ", "+", regex=True)
df["URL"] = 'https://www.youtube.com/results?search_query=' + \
    df['URL'].astype(str)

df2 = df["URL"]
df2.to_csv('shazam2youtube.csv')
