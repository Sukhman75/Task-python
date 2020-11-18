import pandas as pd
#https://pandas.pydata.org/

def get_merged(df1,df2, join_type,merge_on_col):
    """Function to join dataframe on a column
       you can specify on which column to join and type of join"""
    merge_df = pd.merge(df1, df2, on=merge_on_col,  how=join_type)       
    return merge_df

def get_distinct(df, col_name):
    """Function to delete duplicate values according to a particular column"""
    df = df.drop_duplicates(subset=col_name, keep="first")
    return df

def get_word_ending_with(df, col_name, matcher_str):
    """Function to get data with column string ending with matcher_str"""
    df = df.dropna(subset=[col_name])
    df = df[df[col_name].str.endswith(matcher_str)]
    return df