'''
    File contains the code for the logic of the application
'''
import pandas as pd

# removes unwanted columns and drops dupes.
def cleanupColumns(df):
    # Analyzing the columns ==> output all the columns to a text file:

    # f = open("columns.txt", "a+")
    # cols = df.columns
    # for name in cols:
    #     f.write(name)
    #     f.write("\n")
    # f.close()

    # Columns I want to remove are in removing.txt:
    f2 = open("removing.txt", "r")
    colsToRemove = f2.readlines()
    for i in range(0, len(colsToRemove)):
        thing = colsToRemove[i].rstrip()
        colsToRemove[i] = thing
    f2.close()

    # remove them from the DataFrame:
    print(df.shape)
    colsDeleted = 0
    for col in colsToRemove:
        df = df.drop(columns = [col])
        colsDeleted += 1
    print("Removed {} columns from the dataframe.".format(colsDeleted))
    print(df.shape)
    
    # also, drop any duplicate entries:
    df = df.drop_duplicates()
    return df

# parses through the rows and drops any with certain columns as NaN || None.
# Second Data-Cleaning/Preprocessing function
def validateRowsAndColumns(df):
    pass

def outputColumns():
    f2 = open("removing.txt", "r")
    colsToRemove = f2.readlines()
    f2.close()

    f1 = open("columns.txt", "r+")
    currentColumns = f1.readlines()
    newList = []
    print("first, length is: ", len(currentColumns))
    for word in currentColumns:
        if word in colsToRemove:
            pass
        else:
            newList.append(word)
    print(len(word))
def main():

    df = pd.read_csv('CAP4770\data\original\survey_results_public.csv')
    print("Original shape: {}".format(df.shape))
    # df_unique = df.drop_duplicates()
    # df_unique.to_csv('data\cleaned\data-only-unique-rows.csv', index=False)

    # # QA check - export identified duplicates to a new CSV
    # df_duplicates = df[~df.index.isin(df_unique.index)]
    # df_duplicates.to_csv('data\extracted\data_removed_duplicates.csv', index=False)

    df = cleanupColumns(df)
    print(df)
    print("Postprocessing shape: {}".format(df.shape))
    outputColumns()

main()
