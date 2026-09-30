from student_input import get_student_details
from subject_input import get_subject_details
from priority import get_priority
from study_plan import make_study_plan
from strategy import show_strategy


print("===== SMART STUDY PLANNER =====")

na, n, study_hours = get_student_details()

subjects = []

for i in range(n):

    sub, dif, days = get_subject_details(i)

    pri = get_priority(dif, days)

    subjects.append([sub, dif, days, pri])


print("\n===== SUBJECT ANALYSIS =====")

for sub in subjects:
    print(sub[0], "->", sub[3],
          "Priority |", sub[2], "days left")


make_study_plan(subjects, study_hours)

show_strategy(subjects)


print("\n===== GENERAL TIPS =====")

print("Take short breaks between study sessions.")
print("Keep your phone away during focused study.")
print("Revise high-priority subjects regularly.")
print("Stay hydrated and avoid unnecessary stress.")

print("\nStudy plan generated successfully,", na)

