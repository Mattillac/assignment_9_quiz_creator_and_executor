#TITLE:assignment_9_quiz_creator
#asks the user to input a quiz name and number of questions
#enter quiz name:
quiz_name = input("Enter the quiz name: ")
file_reader = open(quiz_name, "w")
#enter a question:
question_maker = input("Enter a question: ")
answer_sheet = input("Enter the answer sheet like this (a, b, c, d (a) ) and enclose with parenthesis the correct answer!: ")
#asks for the possible four answers for ex. (a, b, c, d) and it must include the correct answer
#enter the correct answer:
file_reader.write(question_maker + "\n")
file_reader.write(answer_sheet + "\n\n")
file_reader.close()
#it must write the collected data and convert it into a .txt file, and must ask continuously until the user says no/exit
#create more? yes/no

