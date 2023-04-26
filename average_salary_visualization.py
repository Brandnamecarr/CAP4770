import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv("data/cleaned/data-cleaned.csv")

# Filter the data to only include the relevant education values
relevant_educations = [
    "Bachelor’s degree (BA, BS, B.Eng., etc.)",
    "Associate degree",
    "Some college/university study without earning a degree",
    "Master’s degree (MA, MS, M.Eng., MBA, etc.)",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
    "NA",
]
df = df[df["FormalEducation"].isin(relevant_educations)]

# Group the data by education type and calculate the average salary for each group
grouped = df.groupby("FormalEducation")["Salary"].mean().reset_index()

# Create a bar plot of the average salary by education type
plt.figure(figsize=(10, 6))
plt.bar(grouped["FormalEducation"], grouped["Salary"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Education Type")
plt.ylabel("Average Salary")
plt.title("Average Salary by Education Type")

# Save the plot as an image
plt.savefig("static/average_salary.png")
