def get_subject_details(i):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")

    while True:
        difficulty = input("Difficulty (easy/medium/hard): ").lower()

        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break
        else:
            print("Invalid difficulty. Please enter easy, medium or hard.")

    days = int(input("Days left for exam: "))

    return subject, difficulty, days 
