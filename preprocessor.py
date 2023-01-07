import pandas as pd

df=pd.read_csv('country_wise_latest (3).csv')

def processor(df):

    df.drop(columns=['Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','Confirmed last week','1 week change','1 week % increase','WHO Region'],inplace=True)

    df.rename(columns={'Country/Region':'country'},inplace=True)

    return df

