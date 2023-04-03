'''
    File contains the code for the logic of the application
'''
import os
import json
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

# create a log file for program operations
logFile = open('data/logs/LOG.txt', "a+")

# test function for api to ensure that operations.py can send data to app.py
def apiTest():
    return "Test from operations.py"

# Analyzing the columns ==> output all the columns to a text file:
def output_column_names(df):
    f = open("data/misc/columns.txt", "a+")
    cols = df.columns
    for name in cols:
        f.write(name)
        f.write("\n")
    f.close()

# removes unwanted columns and drops dupes.
def remove_columns_bulk(df):
    # Undesirable columns are in data/misc/removing.txt:
    f2 = open("data/misc/removing.txt", "r")
    colsToRemove = f2.readlines()
    for i in range(0, len(colsToRemove)):
        thing = colsToRemove[i].rstrip()
        colsToRemove[i] = thing
    f2.close()

    # remove them from the DataFrame:
    print(df.shape)
    colsDeleted = 0
    for col in colsToRemove:
        try:
            df = df.drop(columns = [col])
            colsDeleted += 1
        except:
            print("Error removing {} from the DataFrame.".format(col))
    print("Removed {} columns from the dataframe.".format(colsDeleted))
    print(df.shape)
    
    # also, drop any duplicate entries:
    df = df.drop_duplicates()
    return df

def calc_column_difference(columnFile, removedFile):
    # reading in all the comments
    columns = open(columnFile, "r")
    columnList = columns.readlines()
    for i in range (0, len(columnList)):
        tempStr = columnList[i].rstrip()
        columnList[i] = tempStr 
    columns.close()

    # reading in all the removed columns
    removed = open(removedFile, "r")
    removedcols = removed.readlines()
    for i in range(0, len(removedcols)):
        tempStr = removedcols[i].rstrip()
        removedcols[i] = tempStr
    removed.close()
    
    kept_columns = []
    kept_column_filepath = "data/misc/useful_columns.txt"
    for item in columnList:
        if item not in removedcols:
            kept_columns.append(item)
    
    outFile = open(kept_column_filepath, "a+")
    for item in kept_columns:
        outFile.write(item)
        outFile.write("\n")
    outFile.close()
    
# parses through the rows and drops any with certain columns as NaN || None.
# Second Data-Cleaning/Preprocessing function
def validate_rows(df):
    currency_counts = {}
    for index, row in df.iterrows():
        if row['Currency'] in currency_counts:
            currency_counts[row['Currency']] += 1
        else:
            currency_counts[row['Currency']] = 1
    
    salary_counts = {}
    for index, row in df.iterrows():
        if row['Currency'] == 'U.S. dollars ($)':
            if row['Salary'] in salary_counts:
                salary_counts[row['Salary']] += 1
            else:
                salary_counts[row['Salary']] = 1
    with open('convert.txt', 'w') as convert_file:
        convert_file.write(json.dumps(currency_counts))
    convert_file.write("\n")
    convert_file.write("============================================================\n")
    with open('convert.txt', 'w') as convert_file:
        convert_file.write(json.dumps(salary_counts))
    try:
        del salary_counts['NaN']
    except:
        print("Unable to remove NaN")
    print(max(salary_counts, key=salary_counts.get))




# helper function to check if a file exists.
def checkFile(filePath):
    if os.path.isfile(filePath):
        print("Exists")
    else:
        print("DNE")

# machine learning function for Support Vector Regression
def svr_regression(df, career, experience, state, degreeType, technology):
    X = '' # have to identify the columns that predict Y
    Y = '' # have to identify which column is Y
    regr = svm.SVR()
    x_test, y_test, x_train, y_train = train_test_split(X, Y)
    regr.predict([[career, experience, state, degreeType, technology]])

def main():
    filepath = 'data/original/survey_results_public.csv'
    checkFile(filepath)

    # read in the df from the CSV file.
    df = pd.read_csv(filepath, low_memory=False)
    
    df = remove_columns_bulk(df) 

    #calc_column_difference("data/misc/columns.txt", "data/misc/removing.txt")

    validate_rows(df)

    # print("Original shape: {}".format(df.shape))
    # df_unique = df.drop_duplicates()
    # df_unique.to_csv('data\cleaned\data-only-unique-rows.csv', index=False)

    # # QA check - export identified duplicates to a new CSV
    # df_duplicates = df[~df.index.isin(df_unique.index)]
    # df_duplicates.to_csv('data\extracted\data_removed_duplicates.csv', index=False)

main()
