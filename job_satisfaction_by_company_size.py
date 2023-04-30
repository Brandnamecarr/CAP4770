import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned/data-cleaned.csv")

satisfaction_mapping = {
    "Extremely satisfied": 7,
    "Moderately satisfied": 6,
    "Slightly satisfied": 5,
    "Neither satisfied nor dissatisfied": 4,
    "Slightly dissatisfied": 3,
    "Moderately dissatisfied": 2,
    "Extremely dissatisfied": 1,
}

df["JobSatisfaction"] = df["JobSatisfaction"].map(satisfaction_mapping)

df = df.dropna(subset=["JobSatisfaction"])

company_size_categories = [
    "Fewer than 10 employees",
    "10 to 19 employees",
    "20 to 99 employees",
    "100 to 499 employees",
    "500 to 999 employees",
    "1,000 to 4,999 employees",
    "5,000 to 9,999 employees",
    "10,000 or more employees",
]

df = df[df["CompanySize"].isin(company_size_categories)]

plt.figure(figsize=(12, 8))
sns.violinplot(x="CompanySize", y="JobSatisfaction", data=df, cut=0)
plt.title("Job Satisfaction by Company Size")
plt.xlabel("Company Size")
plt.ylabel("Job Satisfaction")
plt.xticks(rotation=45, ha="right")

plt.savefig("ui/src/static/job_satisfaction_by_company_size.png")
