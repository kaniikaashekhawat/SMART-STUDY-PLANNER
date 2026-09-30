print(" === Smart Study Planner === ")

na = input("Enter your name : ")
n = int(input("Enter number of subjects : "))

# Here we take a list to store subjects
subjects = []

for i in range(n):

    print("\nSubject", i + 1)

    sub = input("Enter subject name : ")

    while True:
        dif = input("Difficulty (easy/medium/hard) : ").lower()

        if dif == "easy" or dif == "medium" or dif == "hard" :
            break
        else:
            print("Invalid difficulty. Please enter easy, medium or hard. ")

    days = int(input("Days left for exam : "))
# we are using conditional statements to execute our main program
    if days <= 3:
        pri = "High"

    elif dif == "hard" and days <= 7:
        pri = "High"

    elif dif == "medium" and days <= 7:
        pri = "High"

    elif dif == "hard":
        pri = "Medium"

    else:
        pri = "Low"

    subjects.append([sub, dif, days, pri])
study_hours = int(input("\nEnter daily study hours : "))


print("\nSUBJECT ANALYSIS")

for sub in subjects:
    print(sub[0], "->", sub[3],
          "Priority |", sub[2], "days left")


print("\nPERSONALIZED STUDY PLAN")

for sub in subjects:

    if sub[3] == "High":
        mins = study_hours * 60 // 2

    elif sub[3] == "Medium":
        mins = study_hours * 60 // 3

    else:
        minus = study_hours * 60 // 4

    print(sub[0], ":", mins, "minutes")


print("\nSTUDY STRATEGY")

for sub in subjects:

    if sub[2] <= 3:
        print(sub[0],
              " Focus on revision and important topics.")

    elif sub[2] <= 7:
        print(sub[0],
              " Complete important topics and revise.")

    else:
        print(sub[0],
              " Focus on understanding the concepts.")


print("\nGENERAL TIPS")

print("Take short breaks between study sessions. ")
print("Keep your phone away during focused study. ")
print("Revise high-priority subjects regularly. ")
print("Stay hydrated and avoid unnecessary stress. ")

print("\nStudy plan generated successfully,", na)

