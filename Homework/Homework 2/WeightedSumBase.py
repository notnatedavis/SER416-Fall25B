import csv

# Some constants from the assignment description
POINTS_POSIBLE_QUIZZES = 120
POINTS_POSSIBLE_HOMEWORK = 150
POINTS_POSSIBLE_TEAM_PROJECT = 55
POINTS_POSSIBLE_FINAL_EXAM = 80
WEIGHT_QUIZ = 0.15
WEIGHT_HOMEWORK = 0.25
WEIGHT_TEAM_PROJECT = 0.25
WEIGHT_FINAL_EXAM = 0.35

# If you renamed the file you will need to update this to match
FILE_NAME = "Python-HW-WeightedSums-Data.csv"


def csv_read() -> list:
    """
        Reads the data from the csv and compiles it into a LIST OF DICTIONARIES!
        This means every entry in the list is a dict which can be accessed like a map from Java
        Each entry in the list will be one student from the data
        Each key in the dicts will be the columns names from the csv (name, and the four asessments)
        Example: print(results[0]["Name"]) would print "Student 1"

        You are NOT expected to edit this function at all

    :return: The list of dicts of student data
    """
    with open(FILE_NAME, 'r') as data:
        csv_reader = csv.DictReader(data)
        results = [row for row in csv_reader]
    return results

def question_one_grade_calculation(data) -> None:
    """
    Implement your solution to question 1 here.
    :param data: The list of dicts of student data
    :return: None
    """
    for student in data :
        # convert scores to int
        quiz_score = int(student["Quizzes"])
        hw_score = int(student["Homework"])
        project_score = int(student["Team Project"])
        final_score = int(student["Final Exam"])
        
        # calculate weighted scores (w/ extra credit over 100%)
        quiz_weighted = (quiz_score / POINTS_POSIBLE_QUIZZES) * WEIGHT_QUIZ
        hw_weighted = (hw_score / POINTS_POSSIBLE_HOMEWORK) * WEIGHT_HOMEWORK
        project_weighted = (project_score / POINTS_POSSIBLE_TEAM_PROJECT) * WEIGHT_TEAM_PROJECT
        final_weighted = (final_score / POINTS_POSSIBLE_FINAL_EXAM) * WEIGHT_FINAL_EXAM
        
        # calculate final grade as percentage
        final_grade = (quiz_weighted + hw_weighted + project_weighted + final_weighted) * 100
        
        print(f"{student['Name']} has a grade of {final_grade:.2f}% in the course.")

def question_two_grade_needed_on_final(data) -> None:
    """
    Implement your solution to question 2 here.
    :param data: The list of dicts of student data
    :return: None
    """
    students_without_final = [s for s in data if int(s["Final Exam"]) == 0]
    
    if not students_without_final :
        print("All students have a Final score.")
        return
    
    for student in students_without_final :
        # calculate current grade without final
        quiz_score = int(student["Quizzes"])
        hw_score = int(student["Homework"])
        project_score = int(student["Team Project"])
        
        quiz_weighted = (quiz_score / POINTS_POSIBLE_QUIZZES) * WEIGHT_QUIZ
        hw_weighted = (hw_score / POINTS_POSSIBLE_HOMEWORK) * WEIGHT_HOMEWORK
        project_weighted = (project_score / POINTS_POSSIBLE_TEAM_PROJECT) * WEIGHT_TEAM_PROJECT
        
        current_grade = (quiz_weighted + hw_weighted + project_weighted) * 100
        
        # calculate needed final score to reach 90% overall
        # current_grade/100 + (final_score/80) * 0.35 >= 0.90
        # final_score >= (0.90 - current_grade/100) * (80 / 0.35)
        needed_final_percentage = (0.90 - current_grade/100) / WEIGHT_FINAL_EXAM
        
        if needed_final_percentage > 1.0 :
            # even perfect score (100%) on final won't be enough
            print(f"{student['Name']} cannot get an A in the course.")
        else :
            needed_final_score = needed_final_percentage * POINTS_POSSIBLE_FINAL_EXAM
            # Round up to nearest whole point since scores are integers
            needed_final_score = int(needed_final_score) + (1 if needed_final_score % 1 > 0 else 0)
            print(f"{student['Name']} needs a score of at least {needed_final_score} on the final to get an A.")

def question_three_weakness(data) -> None:
    """
    Implement your solution to question 1 here.
    :param data: The list of dicts of student data
    :return: None
    """
    assessment_names = {
        "Quizzes": (POINTS_POSIBLE_QUIZZES, WEIGHT_QUIZ),
        "Homework": (POINTS_POSSIBLE_HOMEWORK, WEIGHT_HOMEWORK),
        "Team Project": (POINTS_POSSIBLE_TEAM_PROJECT, WEIGHT_TEAM_PROJECT),
        "Final Exam": (POINTS_POSSIBLE_FINAL_EXAM, WEIGHT_FINAL_EXAM)
    }
    
    for student in data :
        # calculate lost points for each assessment (weighted)
        lost_points = {}
        
        for assessment, (max_points, weight) in assessment_names.items() :
            score = int(student[assessment])
            # points lost as percentage of possible, then weighted
            percentage_lost = max(0, (max_points - score) / max_points)
            lost_points[assessment] = percentage_lost * weight
        
        # check for perfect score
        total_lost = sum(lost_points.values())
        if total_lost == 0 :
            print(f"{student['Name']} got a perfect score in the course.")
            continue
        
        # find maximum lost points
        max_loss = max(lost_points.values())
        worst_assessments = [assess for assess, loss in lost_points.items() if loss == max_loss]
        
        if len(worst_assessments) > 1 :
            print(f"{student['Name']} had multiple areas that held them back.")
        else :
            print(f"{student['Name']} lost the most score in {worst_assessments[0]}.")

def question_four_equal_students(data) -> None:
    """
    Implement your solution to question 1 here.
    :param data: The list of dicts of student data
    :return: None
    """
    found_match = False
    
    for i in range(len(data)) :
        for j in range(i + 1, len(data)) :
            student1 = data[i]
            student2 = data[j]
            
            # compare all scores
            if (student1["Quizzes"] == student2["Quizzes"] 
                and student1["Homework"] == student2["Homework"] 
                and student1["Team Project"] == student2["Team Project"] 
                and student1["Final Exam"] == student2["Final Exam"]) :

                print(f"Match found: {student1['Name']} and {student2['Name']} have the same scores.")
                found_match = True

                break
        
        if found_match :
            break
    
    if not found_match :
        print("No students had matching scores.")

def main() -> None:
    """
    The main function, used to grab the data and pass it to
    your answer functions. You are not expected to edit this
    as part of the assignment. Feel free to edit it if needed
    while testing, but remember that the graders will be using
    this exact version when grading your answers.
    :return:
    """
    data = csv_read()
    question_one_grade_calculation(data)
    question_two_grade_needed_on_final(data)
    question_three_weakness(data)
    question_four_equal_students(data)

# Run main automatically if this file is run directly - DO NOT EDIT
if __name__ == '__main__':
    main()
