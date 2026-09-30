def make_study_plan(subjects, study_hours):

    print("\n====== PERSONALIZED STUDY PLAN ======")

    for sub in subjects:

        if sub[3] == "High":
            mins = study_hours * 60 // 2

        elif sub[3] == "Medium":
            mins = study_hours * 60 // 3

        else:
            mins = study_hours * 60 // 4

        print(sub[0], ":", mins, "minutes")
