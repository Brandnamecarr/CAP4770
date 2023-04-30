import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/data-cleaned.csv")

relevant_educations = [
    "Bachelor’s degree (BA, BS, B.Eng., etc.)",
    "Associate degree",
    "Some college/university study without earning a degree",
    "Master’s degree (MA, MS, M.Eng., MBA, etc.)",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
    "NA",
]
df = df[df["FormalEducation"].isin(relevant_educations)]

grouped = df.groupby("FormalEducation")["Salary"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(grouped["FormalEducation"], grouped["Salary"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Education Type")
plt.ylabel("Average Salary")
plt.title("Average Salary by Education Type")

plt.savefig("ui/src/static/average_salary.png")
