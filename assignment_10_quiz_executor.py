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
            question = lines[i][2:].strip()
            i += 1
            if i < len(lines) and lines[i].startswith("A:"):
                answers = lines[i][2:].strip().split(",")
                answers = [answer.strip() for answer in answers]
                quiz_questions.append({
                    "question": question,
                    "answers": answers
                })
                i += 1
    else:
        i+= 1

    return quiz

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

 
 #Prints the question (Who is the pirate in pirates of the carribean with a bird name?)
 # prints the possible answers (1. Jack Sparrow, 2. Captain Hook, 3. Davy Jones, 4. Blackbeard)
 #User will answer the question and the program will check if the answer is correct or not. 
 #If wrong kindly state the the user is wrong, but if correct, kindly state the user is correct.
 #asks the user if he wants to continue to answer more quizzes or not.