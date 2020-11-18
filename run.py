import pandas as pd
#https://pandas.pydata.org/
import dataPreprocess

#Defining variable to print '$' multiple times
seperator_multiplier = 65

#Reading the data
user1_df = pd.read_csv("user1.csv")
user2_df = pd.read_csv("user2.csv")

if __name__ == "__main__":
    #get the users which are common in both the csv files into 1 data frame and print the first 5 lines to terminal
    print('$'*seperator_multiplier, '\n')
    try:
        merged_users_inner = dataPreprocess.get_merged(user2_df, user1_df, join_type='inner',merge_on_col='uid')
        print('Users which are common:\n', merged_users_inner.head())
    except Exception as e:
        print(e)
    
    #get the users which are not common in both the csv files and put them in a dataframe and print the first 5 lines to terminal    
    print('$'*seperator_multiplier, '\n')
    try:
        merged_users_outer = dataPreprocess.get_merged(user1_df, user2_df, join_type='outer',merge_on_col='uid')
        uncommon_users = merged_users_outer[~merged_users_outer['uid'].isin(merged_users_inner['uid'])]
        print('Users which are not common:\n',uncommon_users.head())
    except Exception as e:
        print(e)

    #get all the distinct users from both the tables and put them in a dataframe and print the first 5 lines to terminal
    print('$'*seperator_multiplier, '\n')
    try:
        distinct_user1 = dataPreprocess.get_distinct(user1_df, col_name='uid')
        distinct_user2 = dataPreprocess.get_distinct(user2_df, col_name='uid')
        merged_distinct_users = dataPreprocess.get_merged(distinct_user1, distinct_user2, join_type='outer',merge_on_col='uid')
        print('Distinct users from both the tables in one data frame:\n', merged_distinct_users.head())
    except Exception as e:
        print(e)
    
    #get all the users who have their email addresses ending in a .com and put them in a dataframe and print the first 5 lines of it to the termi    
    print('$'*seperator_multiplier, '\n')    
    try:
        print('users who have their email addresses ending in a .com:\n', dataPreprocess.get_word_ending_with(user1_df, col_name='email', matcher_str='.com').head())
    except Exception as e:
        print(e)     