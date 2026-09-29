def make_study_plan(subjects, study_hours):

    print("\n===== PERSONALIZED STUDY PLAN =====")

    for subject in subjects:

        if subject[3] == "High":
            minutes = study_hours * 60 // 2

        elif subject[3] == "Medium":
            minutes = study_hours * 60 // 3

        else:
            minutes = study_hours * 60 // 4

        print(subject[0], ":", minutes, "minutes")
