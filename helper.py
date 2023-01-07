import pandas as pd

df=pd.read_csv('country_wise_latest (3).csv')




def country_list(df):
    new_df = df['country'].unique().tolist()
    new_df.insert(0, 'Overall')

    return new_df



def country_wise(df,region):
    temp_df = df
    if region == 'Overall':
        temp_df = df

    if region != 'Overall':
        temp_df = temp_df[temp_df['country'] == region]

    return(temp_df)








