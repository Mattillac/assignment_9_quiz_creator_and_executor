#QUIZ EXECUTOR
import random

#Opens the file and reads the questions and answers
def quiz_loader_data(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return quiz_questions
    
i = 0
while i < len(lines):
        if lines[i].startswith("Q:"):
            question = lines[i][9:].strip()
            i += 1
            if i < len(lines) and lines[i].startswith("Answers and Correct Answer():"):
                answer_line = lines[i][28:].strip().split(",")
          if "(" in answer_line: and ")" in answer_line:
            last_parenthesis = answer_line.find(")")
            correct = answer_line[last_parenthesis+1:answer_line.rfind(",")].strip()
            answers = [answer.strip() for answer in answer_line[:last_parenthesis].split(",") if answer.strip()]
            if correct not in answers:
                answers.append(correct)

            quiz.append({
                "question": question,
                "answers": answers,
                "correct": correct
            })
         i += 1
    else:
        i+= 1

    return quiz

 #Prints the question (Who is the pirate in pirates of the carribean with a bird name?)
def run_quiz(quiz):
    if not quiz:
        print("No valid quiz questions found in the file.")
        return

    score = 0
    results = []
    random.shuffle(quiz)  # Shuffle all questions

    for index, q in enumerate(quiz, start=1):
        print(f"\nQuestion {index}: {q['question']}")

        # Prepare and shuffle answers
        answers = q['answers'][:]
        random.shuffle(answers)
        
        # Display answers with numbers
        for i, answer in enumerate(answers, start=1):
            print(f"  {i}. {answer}")

        # Get and validate user input
        while True:
            try:
                choice = input(f"Your answer (1-{len(answers)}): ").strip()
                if not choice:
                    raise ValueError
                
                choice = int(choice)
                if 1 <= choice <= len(answers):
                    selected = answers[choice - 1]
                    correct = selected == q['correct']
                    
                    if correct:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {q['correct']}")
                    
                    results.append((q['question'], selected, q['correct'], correct))
                    break
                else:
                    print(f"Please enter a number between 1 and {len(answers)}")
            except ValueError:
                print("Please enter a valid number.")

    # Display final results
    print(f"\Quiz complete! Your score: {score}/{len(quiz)}")
    print("\n Detailed Results:")

    for i, (question, your_answer, correct_answer, is_correct) in enumerate(results, start=1):
        status = "Correct" if is_correct else "Incorrect"
        print(f"\n{i}. {question}")
        print(f"   Your answer: {your_answer}")
        print(f"   Correct answer: {correct_answer}")
        print(f"   Result: {status}")



 #Enter the file name: 
 def main_engine():
    print("HEY! WELCOME TO THE QUIZ EXECUTOR")
    file_name = input("Enter the file name to start: ")
    quiz_infos = quiz_loader_data(file_name)
    if quiz_infos:
        run_quiz(quiz_infos)
    else:
        print("Failed to load quiz. Please check the file name and try again.")
if __name__ == "__main__":
    main_engine()

 

 # prints the possible answers (1. Jack Sparrow, 2. Captain Hook, 3. Davy Jones, 4. Blackbeard)
 #User will answer the question and the program will check if the answer is correct or not. 
 #If wrong kindly state the the user is wrong, but if correct, kindly state the user is correct.
 #asks the user if he wants to continue to answer more quizzes or not.