import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/data-cleaned.csv")

relevant_educations = [
    "Bachelor’s degree (BA, BS, B.Eng., etc.)",
    "Associate degree",
    "Some college/university study without earning a degree",
    "Master’s degree (MA, MS, M.Eng., MBA, etc.)",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
    "NA",]

df = df[df["FormalEducation"].isin(relevant_educations)]

grouped_country = df.groupby("Country").count().reset_index()
top_countries = grouped_country.sort_values(by="Respondent", ascending=False).head(10)

boxplot_data = []
for country in top_countries["Country"]:
    country_data = df[df["Country"] == country]["Salary"]
    boxplot_data.append(country_data.dropna().values)

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(boxplot_data, labels=top_countries["Country"])

ax.set_xlabel("Country")
ax.set_ylabel("Salary")
ax.set_title("Salary Distribution by Top Countries")

plt.savefig("ui/src/static/salary_by_top_countries.png")
