#TITLE:assignment_9_quiz_creator
#asks the user to input a quiz name and number of questions
#enter quiz name:
quiz_name = input("Enter the quiz name: ")
file_reader = open(quiz_name, "a")
if not quiz_name.endswith(".txt"):
    quiz_name += ".txt"
while True:
    #enter a question:
    question_maker = input("Enter a question: ")
    answer_sheet = input("Enter the answer sheet like this (a, b, c, d (a) ) and enclose with parenthesis the correct answer!: ")
    #asks for the possible four answers for ex. (a, b, c, d) and it must include the correct answer
    #enter the correct answer:
    file_reader.write("Question: " + question_maker + "\n")
    file_reader.write("Answers and Correct Answer""(): " + answer_sheet + "\n\n")

    program_buster = input("Do you want to add more questions? [YES/NO]: ").upper()
    #it must write the collected data and convert it into a .txt file, and must ask continuously until the user says no/exit
    if program_buster == "YES":
        continue
    elif program_buster == "NO":
        break
    else:
        print("SHAME ON YOU WHY YOU DIDN'T FOLLOWED THE INSTRUCTIONS")
        break
    #create more? yes/no
file_reader.close()
print("file is saved! thank you for using this program")
#additonal note