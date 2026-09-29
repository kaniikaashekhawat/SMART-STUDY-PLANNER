def show_strategy(subjects):

    print("\n STUDY STRATEGY ")

    for subject in subjects:

        if subject[2] <= 3:
            print(subject[0],
                  "-> Focus on revision and important topics.")

        elif subject[2] <= 7:
            print(subject[0],
                  "-> Complete important topics and revise.")

        else:
            print(subject[0],
                  "-> Focus on understanding concepts.")
