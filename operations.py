'''
    File contains the code for the logic of the application
'''
# random imports
import os
import json

# important Data Science Libraries:
import pandas as pd
import numpy as np

# important Machine Learning Libraries:
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn import tree
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# create a log file for program operations
logFile = open('data/logs/LOG.txt', "a+")

# test function for api to ensure that operations.py can send data to app.py
def apiTest():
    return "Test from operations.py"

# read column txt file.
def read_column_file():
    inFile = open("data/misc/columns.txt", "r+")
    bleh = inFile.readlines()
    for i in range (0, len(bleh)):
        bleh[i] = bleh[i].rstrip()
    return bleh

# Analyzing the columns ==> output all the columns to a text file:
def output_column_names(df):
    f = open("data/misc/columns.txt", "a+")
    cols = df.columns
    for name in cols:
        f.write(name)
        f.write("\n")
    f.close()

# helper function to check if a file exists.
def checkFile(filePath):
    if os.path.isfile(filePath):
        print("Exists")
    else:
        print("DNE")

# function to convert the 'DevType' column into Software/Data/Management categories.
def format_DevType_Column(df):
    sw_Count = 0
    ds_count = 0
    mgmt_count = 0
    stu_count = 0
    misc_count = 0
    DevTypeList = [] # will contain strings
    # iterate through the dataframe.
    for i, j in df.iterrows():
        # get the current type of developer.
        current_entry = j['DevType']
        newStr = DevType_Converter(current_entry)
        DevTypeList.append(newStr)
        if newStr == 'Software':
            sw_Count += 1
        elif newStr == 'Data Science':
            ds_count += 1
        elif newStr == 'Management':
            mgmt_count += 1
        elif newStr == 'Student':
            stu_count += 1
        elif newStr == 'Miscellaneous':
            misc_count += 1
    print("sw_Count: {}, ds_count: {}, mgmt_count: {}, stu_count: {}, misc_count: {}".format(sw_Count, ds_count, mgmt_count, stu_count, misc_count))
    sum = sw_Count + ds_count + mgmt_count + stu_count + misc_count
    print("Counted(sum): {}, lenStringsDevType: {}".format(sum, len(DevTypeList)))
    
    df['DevType'] = DevTypeList
    return df
        
# helper function to return new string.
# find() function returns -1 if string is not found.
def DevType_Converter(s):
    # software checks
    if s.find('Back-end') != -1:
        if s.find('Data') == -1 or s.find('data') == -1: 
            return "Software"
        elif s.find('Data') != -1 or s.find('data') != -1:
            return 'Data Science'
        
    elif s.find('Front-end') != -1:
        if s.find('Data') == -1 or s.find('data') == -1: 
            return 'Software'
        elif s.find('Data') != -1 or s.find('data') != -1:
            return 'Data Science'
        
    elif s.find('Full-stack') != -1:
        if s.find('Data') == -1 or s.find('data') == -1: 
            return 'Software'
        elif s.find('Data') != -1 or s.find('data') != -1:
            return 'Data Science'
        
    elif s.find('Mobile') != -1:
        return "Software"
    
    elif s.find('Embedded applications') != -1 or s.find('devices developer') != -1:
        return "Software"
        
    # data science checks
    elif s.find('Data') != -1 or s.find('data') != -1:
        return "Data Science"
    
    elif s.find('Database') != -1 or s.find('maching learning') != -1 or s.find('Machine Learning') != -1:
        return 'Data Science'
        
    # management roles
    elif s.find('Manager') != -1 or s.find('C-suite') != -1 or s.find('executive') != -1 or s.find('manager') != -1:
        return "Management"
    
    # student entries
    elif s.find('Student') != -1:
        return "Student"
    
    # error catching & logging
    else:
        #print ('UNABLE TO MATCH {}'.format(s))
        return "Miscellaneous"


# testing DevType_Converter:
def test_DevType_Converter():
    # TEST 1: should return "Software"
    s = "Back-end" 
    testStr = DevType_Converter(s)
    print('Test 1: got back: {}'.format(testStr))
    try:
        assert testStr == 'Software', 'Function should return Software'
        print('Test 1 Passed')
    except:
        print("Test 1 failure: test_DevType_Converter")
    print()
    
    # TEST 2: should return 'Data science'
    s = "Database specialist"
    testStr = DevType_Converter(s)
    print('Test 2: got back: {}'.format(testStr))
    try:
        assert testStr == 'Data Science', 'Function should return Data Science'
        print('Test 2 Passed')
    except:
        print('Test 2 failure: test_DevType_Converter')
    print()
    
    # TEST 3: should return "Management"
    s = 'Product Manager'
    testStr = DevType_Converter(s)
    print('Test 3: got back: {}'.format(testStr))
    try:
        assert testStr == 'Management', 'Function should return Management'
        print('Test 3 Passed')
    except:
        print("Test 3 failure: test_DevType_Converter")
    print()
    
    # complex search term: 
    # TEST 4: should return 'Software'
    s = 'Front-end; Database Applications Developer'
    testStr = DevType_Converter(s)
    print('Test 4: got back: {}'.format(testStr))
    try:
        assert testStr == 'Software', 'Function should return Software'
        print('Test 4 Passed')
    except:
        print('Test 4 failure: test_DevType_Converter')
    print()

# YearsExperience_Converter(df)
def YearsExperience_Converter(df):
    yearsList = []
    for i, j in df.iterrows():
        value = j['YearsCoding']
        value = value.replace(' years', '')
        value = value.replace(' or more', '+')
        if value.find('nan') != -1:
            print("HERE")
            value = '0'
        yearsList.append(value)
    df['YearsCoding'] = yearsList
    return df

# Education_Converter
def Education_Converter(df):
    # educations holds the extracted 
    educations = []
    for i, j in df.iterrows():
        value = j['FormalEducation']
        if value.find('Some') != -1:
            educations.append('Some College/No Degree')
        
        elif value.find('Associate') != -1:
            educations.append("Associate's")
            
        elif value.find("Bachelor") != -1:
            educations.append("Bachelor's")
            
        elif value.find("Maste") != -1:
            educations.append("Master's")
            
        elif value.find('doctoral') != -1:
            educations.append("Doctoral")
            
        elif value.find('Secondary') != -1:
            educations.append('Secondary (High School)')
        
        elif value.find('I never completed') != -1:
            educations.append('None')
            
        elif value.find('Primary') != -1:
            educations.append('Elementary')
        
        elif value.find('Professional') != -1:
            educations.append('Professional (JD, MD, etc.)')
        else: 
            print(value)
    
    df['FormalEducation'] = educations
    return df

# salary formatter:
def Salary_Formatter(df):
    # first remove nan entries from the dataframe.
    df = Helper_Salary_Formatter(df)
    
    # calculate average (so skewed rn, not sure why)
    avg = df['Salary'].mean()
    # print (avg)
    
    # convert from float to int
    conv_list = []
    for i, j in df.iterrows():
        conv_list.append(int(j['Salary']))
    
    # return df with formatted salary column
    return df 

# salary formatter helper:
def Helper_Salary_Formatter(df):
    noNans = []
    for i, j in df.iterrows():
        temp = j['Salary']
        if temp == 'nan':
            noNans.append(0)
        else:
            try:
                noNans.append(float(temp))
            except:
                
                if temp.find('.') != -1:
                    temp = temp.replace('.', '')
                    if temp.find(',') != -1:
                        temp = temp.replace(',', '')
                    noNans.append(float(temp))
                    
                elif temp.find(',') != -1:
                    temp = temp.replace(',', '')
                    noNans.append(float(temp))
    for i in range(0, len(noNans)):
        if noNans[i] < 75000:
            noNans[i] += 25000
        elif noNans[i] > 1000000:
            noNans[i] = noNans[i] / 100
        elif noNans[i] == 0:
            noNans[i] = 50000
    df['Salary'] = noNans
    return df

# ML Function
# will add parameters here to format the 'input' from the form on the React site.
def predict_salary(df): 
    print("Data types:")
    print(df.dtypes)
    # need to encode some features so the model will run correctly
    le = preprocessing.LabelEncoder()
    originalValues = df['DevType'].tolist() # catch OG values from DEVTYPE column.
    #df['DevType'] = le.fit_transform(df['DevType'])
    le.fit(df['DevType'])
    #print(type(le.classes_))
    encoded_labels = le.transform(df['DevType'])
    df['DevType'] = encoded_labels
    
    # encode the YearsExperience
    le_YE = preprocessing.LabelEncoder()
    originalValues_YE = df['YearsCoding'].tolist()
    le_YE.fit(df['YearsCoding'])
    YE_encoded_labels = le_YE.transform(df['YearsCoding'])
    df['YearsCoding'] = YE_encoded_labels
    
    # encode the FormalEducation column
    le_FE = preprocessing.LabelEncoder()
    originalValues_FE = df['FormalEducation'].tolist()
    le_FE.fit(df['FormalEducation'])
    FE_encoded_labels = le_FE.transform(df['FormalEducation'])
    df['FormalEducation'] = FE_encoded_labels
    
    # encode the LanguagesWorkWith column
    le_PL = preprocessing.LabelEncoder()
    originalValues_PL = df['LanguageWorkedWith'].tolist()
    le_PL.fit(df['LanguageWorkedWith'])
    PL_encoded_labels = le_PL.transform(df['LanguageWorkedWith'])
    df['LanguageWorkedWith'] = PL_encoded_labels
    
    le_salary = preprocessing.LabelEncoder()
    originalValues_sal = df['Salary'].tolist()
    le_salary.fit(df['Salary'])
    salary_encoded_labels = le_salary.transform(df['Salary'])
    df['Salary'] = salary_encoded_labels
    
    
    # set x & y to the respective data columns.
    X = df[['DevType','YearsCoding', 'FormalEducation', 'LanguageWorkedWith']]
    Y = df[['Salary']]
    
    # call test_train_split 
    x_train, x_test, y_train, y_test = train_test_split(X, Y)
    
    
#     # initialize and train the model using SVM classifier (SVC)
    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    # calculate the accuracy score of the model
    score = clf.score(x_test, y_test)
    print("Score: {}".format(score))
    
    clf2 = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf2.fit(x_train, y_train)
    score2 = clf2.score(x_test, y_test)
    print("Score2: {}".format(score2))
    
    
    return df


# machine learning function for Support Vector Regression
def svr_regression(df, career, experience, state, degreeType, technology):
    X = '' # have to identify the columns that predict Y
    Y = '' # have to identify which column is Y
    regr = None
    x_test, y_test, x_train, y_train = train_test_split(X, Y)
    regr.predict([[career, experience, state, degreeType, technology]])

def main():
    #test_DevType_Converter()
    # print(os.getcwd())
    # checkFile('data/original/survey_results_public.csv')
    # get the list of columns
    columnList = read_column_file()

    # import the CSV file.
    df = pd.read_csv('data/original/survey_results_public.csv', low_memory=False, index_col=False)

    # drop rows where country != 'United States'
    df_new = df[df['Country'] == 'United States']

    # drop unnecessary columns from the data frame.
    df1 = df_new[['DevType','YearsCoding', 'FormalEducation', 'LanguageWorkedWith', 'Salary']]
    df1 = df1.dropna()

    # running into data problems, need to reformat some of the data values to help with prediction
    df2 = df1.copy()

    # branches to function to format DevType column. Replaces the DevType column in the df.
    df2 = format_DevType_Column(df2)
    print(df2.columns)
    df2 = YearsExperience_Converter(df2)
    df2 = Education_Converter(df2)
    df2 = Salary_Formatter(df2)

    df2 = predict_salary(df2)

main()
