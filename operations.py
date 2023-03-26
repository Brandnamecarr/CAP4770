'''
    File contains the code for the logic of the application
'''
import pandas as pd

df = pd.read_csv('data\original\survey_results_public.csv')
df_unique = df.drop_duplicates()
df_unique.to_csv('data\cleaned\data-only-unique-rows.csv', index=False)

# QA check - export identified duplicates to a new CSV
df_duplicates = df[~df.index.isin(df_unique.index)]
df_duplicates.to_csv('data\extracted\data_removed_duplicates.csv', index=False)
