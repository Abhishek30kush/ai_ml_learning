import pandas as pd
import matplotlib.pyplot as plt
#load datatset

df=pd.read_csv("student.csv")

print("Dataset:\n", df)

# Add total and Percentage
df["Total"]=df[["Math", "Physics", "Chemistry", "English"]].sum(axis=1)

df["Percentage"]=df["Total"]/4

print("\nAfter Adding Total and Percentage:\n", df)

# Grade Calculation 

def grade_calc(percent):
    if percent>=90:
        return "A"
    elif percent>=75:
        return "B"
    elif percent>=60:
        return "C"
    else:
        return "Fail"
df["Grade"]=df["Percentage"].apply(grade_calc)

print("\nWith Grades:\n", df)

# Top Performer
top_student=df.sort_values(by="Percentage", ascending=False).iloc[0]
print("\nTop Performer:\n", top_student)

# Subject-wise Average
subject_avg=df[["Math", "Physics", "Chemistry", "English"]].mean()
print("\n Subject-Wise Average:\n", subject_avg)

# Pass Percentage
pass_percent=(df["Grade"]!="Fail").mean()*100
print("\nPass Percentage:", pass_percent)

# Save new file
df.to_csv("students_analysis.csv", index=False)

subject_avg.plot(kind="bar")
plt.title("Subject Average Marks")
plt.ylabel("Marks")
plt.show()