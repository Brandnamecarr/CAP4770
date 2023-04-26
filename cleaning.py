import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv('data/data-only-unique-rows.csv')

# Remove any rows that contain NaN or nan values
df.dropna(subset=['Salary'], inplace=True)

# Check if the 'Salary' column exists in the DataFrame
if 'Salary' in df.columns:
    # Convert the Salary column to a string data type
    df['Salary'] = df['Salary'].astype(str)

    # Remove any rows where the Salary column contains a comma
    df = df[~df['Salary'].str.contains(',')]

    # Convert the Salary column to a numeric data type
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

    # Save the cleaned data to a new CSV file
    df.to_csv('data/cleaned/data-cleaned.csv', index=False)
else:
    print("The 'Salary' column does not exist in the DataFrame.")
