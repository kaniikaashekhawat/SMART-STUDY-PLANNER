# Smart Study Planner

## About the Project

Smart Study Planner is a simple Python project made to help students organize their study time before exams.

When there are several subjects to prepare for, it can be difficult to decide which subject needs more attention. This program takes the subject difficulty, the number of days left for the exam, and the student's available study hours and creates a simple study plan.

I made this project using basic Python concepts so that the program is easy to understand and use.

## What the Program Does

The program asks the student for:

* Name
* Number of subjects
* Daily study hours
* Subject name
* Subject difficulty
* Number of days left for the exam

Based on the difficulty and days left, the program gives each subject a priority:

* **High Priority** – when the exam is very close or the subject needs more attention
* **Medium Priority** – mainly for hard subjects with more time available
* **Low Priority** – when there is comparatively more time or the subject is easier

It then suggests study time for each subject and gives a simple study strategy according to the days left.

## Main Features

* Simple command-line interface
* Takes information directly from the user
* Checks whether the entered difficulty is valid
* Gives priority to subjects
* Suggests study time
* Gives different study strategies based on exam date
* Provides a few general study tips
* Does not require any external Python library

## Technologies Used

* Python 3
* Functions
* Lists
* Loops
* Conditional statements
* User input
* Python modules

## Project Structure

```text
Smart-Study-Planner/
│
├── main.py
├── student_input.py
├── subject_input.py
├── priority.py
├── study_plan.py
└── strategy.py
```

### What Each File Does

**main.py**
This is the main file. It connects all the other files and controls the overall flow of the program.

**student_input.py**
Takes the student's name, number of subjects and daily study hours.

**subject_input.py**
Takes the subject name, difficulty and days left for the exam. It also checks the difficulty entered by the user.

**priority.py**
Decides whether a subject should have High, Medium or Low priority.

**study_plan.py**
Calculates the suggested study time for each subject according to its priority.

**strategy.py**
Displays a suitable study strategy based on the number of days left.

## How to Run the Project

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check it using:

```bash
python --version
```

### 2. Open the Project Folder

Open the project folder in VS Code or any Python-supported editor.

### 3. Run the Main File

Open the terminal in the project folder and run:

```bash
python main.py
```

The program will then ask for the required information.

## Example

A sample interaction can look like this:

```text
===== SMART STUDY PLANNER =====

Enter your name: Kanika
Enter number of subjects: 3
Enter daily study hours: 6

Subject 1
Enter subject name: Calculus
Difficulty (easy/medium/hard): medium
Days left for exam: 5

Subject 2
Enter subject name: Python
Difficulty (easy/medium/hard): hard
Days left for exam: 3

Subject 3
Enter subject name: EVS
Difficulty (easy/medium/hard): easy
Days left for exam: 10
```

The program then shows the priority, suggested study time and study strategy for each subject.

## Requirements

The project only needs:

* Python 3.x
* A computer with a terminal or Python editor

No external packages are required.

## Future Improvements

There are several things that can be added to the project later, such as:

* Saving the generated study plan
* Adding a graphical interface
* Adding a progress tracker
* Adding reminders
* Creating a complete daily timetable

## Conclusion

Smart Study Planner is a small and practical project that uses basic Python concepts to solve a common student problem. The main aim of the project is not to make a complicated planner, but to provide a simple way to decide which subjects need attention and how much study time can be given to them.
