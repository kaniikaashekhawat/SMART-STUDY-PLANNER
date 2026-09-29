from student_input import get_student_details
from subject_input import get_subject_details
from priority import get_priority
from study_plan import make_study_plan
from strategy import show_strategy


print("===== SMART STUDY PLANNER =====")

name, n, study_hours = get_student_details()

subjects = []

for i in range(n):

    subject, difficulty, days = get_subject_details(i)

    priority = get_priority(difficulty, days)

    subjects.append([subject, difficulty, days, priority])


print("\n===== SUBJECT ANALYSIS =====")

for subject in subjects:
    print(subject[0], "->", subject[3],
          "Priority |", subject[2], "days left")


make_study_plan(subjects, study_hours)

show_strategy(subjects)


print("\n===== GENERAL TIPS =====")

print("Take short breaks between study sessions.")
print("Keep your phone away during focused study.")
print("Revise high-priority subjects regularly.")
print("Stay hydrated and avoid unnecessary stress.")

print("\nStudy plan generated successfully,", name)
