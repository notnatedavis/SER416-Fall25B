# SER416 - Fall'25 B
# ndavispe
# exercise3.py

import random

def get_question_count() :
    while True :
        try :
            count = int(input("How many multiplication questions would you like to attempt? (1-50) : "))
            if 1 <= count <= 50 :
                return count
            else :
                print("Enter a number between 1 and 50")
        except ValueError:
            print("Invalid input. Please enter a whole number")


def generate_problem() :
    # generate a random multiplication problem

    factor1 = random.randint(1, 15)
    factor2 = random.randint(1, 15)
    correct_answer = factor1 * factor2

    return factor1, factor2, correct_answer


def get_user_answer(problem_number, factor1, factor2) :
    # prompt user for their answer to a multiplication problem

    try :
        user_input = input(f"Q{problem_number}: {factor1} × {factor2} = ")
        return int(user_input)
    except ValueError :
        print("Please enter a valid number.")
        return None


def evaluate_answer(user_answer, correct_answer) :
    # evaluate if the user's answer is correct and provide feedback
    
    if user_answer == correct_answer :
        print("Correct!")
        return True
    else :
        print(f"Incorrect. The correct answer is {correct_answer}")
        return False


def display_quiz_intro() :
    # Display welcome message and quiz instructions
    print("MULTIPLICATION QUIZ")


def display_final_results(score, total_questions) :
    # Display the final quiz results to the user

    percentage = (score / total_questions) * 100
    
    print("\nQUIZ RESULTS")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {score}")


def run_quiz_questions(question_count) :
    # Execute the main quiz loop with all questions

    score = 0
    
    print(f"\nStarting quiz with {question_count} questions...\n")
    
    for question_num in range(1, question_count + 1) :
        # generate problem
        factor1, factor2, correct_answer = generate_problem()
        
        # get and validate user answer
        user_answer = None
        while user_answer is None :
            user_answer = get_user_answer(question_num, factor1, factor2)
        
        # evaluate answer and update score
        if evaluate_answer(user_answer, correct_answer) :
            score += 1
        
        print()  # empty line for readability
    
    return score, question_count


def ask_for_retry() :
    # ask user if they want to take another quiz

    while True :
        retry = input("\nWould you like to take another quiz? (y/n): ").lower().strip()
        if retry in ['y', 'yes'] :
            return True
        elif retry in ['n', 'no'] :
            return False
        else :
            print("Please enter 'y' for yes or 'n' for no.")


def main() :
    print("Welcome to the Multiplication Quiz Program")
    
    try :
        while True :
            # display introduction
            display_quiz_intro()
            
            # get number of questions
            question_count = get_question_count()
            
            # run the quiz
            score, total_questions = run_quiz_questions(question_count)
            
            # display results
            display_final_results(score, total_questions)
            
            # ask if user wants to retry
            if not ask_for_retry() :
                break
                
    except KeyboardInterrupt :
        print("\n\nQuiz interrupted. Thank you for playing!")
    except Exception as e :
        print(f"\nerror : {e}")

if __name__ == "__main__" :
    main()