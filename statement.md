# Project Statement

## Project Title

**Smart Study Planner**

## Introduction

Managing several subjects before exams can become confusing, especially when every subject has a different level of difficulty and a different exam date.

The Smart Study Planner is a simple Python-based program designed to make this process easier. It takes basic information from a student and uses it to suggest which subjects should be given more attention and how much study time can be given to them.

## Problem Statement

Students often have limited study hours but several subjects to prepare for. Without a proper plan, they may spend too much time on one subject and leave other important subjects for later.

The problem addressed by this project is to create a simple study planning system that considers:

* Difficulty of the subject
* Number of days left for the exam
* Available study hours per day

The program uses these inputs to assign a priority to each subject and provide a basic study plan.

## Objective

The main objective of this project is to create a simple and easy-to-use study planner using basic Python programming concepts.

The project aims to:

1. Collect the student's study-related information.
2. Take the difficulty and exam date of each subject.
3. Assign a suitable priority to each subject.
4. Suggest study time according to the priority.
5. Give a simple study strategy based on the remaining days.
6. Help students organize their preparation in a clearer way.

## Proposed Solution

The program first asks the student for their name, number of subjects and daily study hours.

For every subject, the student enters its name, difficulty and number of days left for the exam. The program then checks these details and assigns a priority.

Subjects with exams approaching soon are given higher attention. Hard subjects with limited preparation time are also given higher priority.

After assigning priorities, the program suggests how many minutes can be spent on each subject. It also provides a study strategy based on the number of days remaining.

## Working of the Project

The basic flow of the project is:

```text
Student Details
      ↓
Subject Details
      ↓
Difficulty + Days Left
      ↓
Priority Assignment
      ↓
Study Time Suggestion
      ↓
Study Strategy
      ↓
General Study Tips
```

The project is divided into different Python files so that each part has a specific responsibility. This also makes the code easier to understand and maintain.

## Technologies and Concepts Used

The project is developed using Python 3.

The main Python concepts used are:

* Functions
* Lists
* `for` loops
* `while` loops
* `if-elif-else` statements
* User input
* Modules
* Basic arithmetic operations

No external libraries are used.

## Expected Outcome

After entering the required details, the student receives:

* A priority for each subject
* Suggested study time
* A study strategy based on days left
* General study tips

The expected outcome is a simple plan that helps the student understand where to focus their available study time.

## Limitations

The current version is a basic command-line application. It does not save the study plan after the program is closed, and it does not track the student's actual progress.

The suggested study time is also based on a simple priority system rather than a detailed personalized timetable.

## Future Scope

The project can be improved in the future by adding features such as:

* Saving study plans
* Progress tracking
* Reminders
* A graphical user interface
* Daily and weekly timetable generation
* More personalized planning options

## Conclusion

The Smart Study Planner demonstrates how basic Python programming concepts can be combined to create a useful application for students.

The project focuses on keeping the solution simple and practical while still solving a real problem: deciding which subjects need attention and organizing the available study time before exams.
