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

years_experience_categories = [
    "0-2 years",
    "3-5 years",
    "6-8 years",
    "9-11 years",
    "12-14 years",
    "15-17 years",
    "18-20 years",
    "21-23 years",
    "24-26 years",
    "27-29 years",
    "30 or more years",
]

colors = {
    relevant_educations[i]: f"C{i}" for i in range(len(relevant_educations))
}

plt.figure(figsize=(12, 8))

for education in relevant_educations:
    education_data = df[df["FormalEducation"] == education]
    
    avg_salaries = [
        education_data[education_data["YearsCoding"] == experience]["Salary"].mean()
        for experience in years_experience_categories
    ]
    
    plt.plot(years_experience_categories, avg_salaries, label=education, color=colors[education])

plt.xticks(rotation=45, ha="right")
plt.xlabel("Years of Experience")
plt.ylabel("Average Salary")
plt.title("Average Salary by Years of Experience and Education Type")
plt.legend()
plt.savefig("ui/src/static/average_salary_by_years_experience.png")
