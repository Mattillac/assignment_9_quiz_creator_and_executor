import random

def load_quiz(filename):
	quiz = []
	try:
		with open(filename, 'r') as file:
			lines = [line.strip() for line in file.readlines() if line.strip()]
	except FileNotFoundError:
		print(f"ERROR! File '{filename}' not found.")
		return quiz

	i = 0
	while i < len(lines):
		if lines[i].startswith("Question:"):
			question = lines[i][len("Question:"):].strip()
			i += 1
			
			if i < len(lines) and lines[i].startswith("Answers and Correct Answer():"):
				answer_line = lines[i][len("Answers and Correct Answer():"):].strip()
				i += 1 
				

				if "(" in answer_line and ")" in answer_line:
					last_paren = answer_line.rfind('(')
					correct_answer = answer_line[last_paren+1:answer_line.rfind(')')].strip()
					all_answers = [a.strip() for a in answer_line[:last_paren].split(',') if a.strip()]
					
				   
					if correct_answer not in all_answers:
						all_answers.append(correct_answer)
					
					quiz.append({
						"question": question,
						"answers": all_answers,
						"correct": correct_answer
					})
			else:
				i += 1
		else:
			i += 1 

	return quiz

def run_quiz(quiz):
	if not quiz:
		print("🚫 No valid quiz questions found in the file.")
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
						print("NICE CORRECT!")
						score += 1
					else:
						print(f"Sorry, NICE TRY THOUGH! The correct answer was: {q['correct']}")
					
					results.append((q['question'], selected, q['correct'], correct))
					break
				else:
					print(f"Please enter a number between 1 and {len(answers)}")
			except ValueError:
				print("Please enter a valid number.")

	# Display final results
	print(f"\n🎉 Quiz complete! Your score: {score}/{len(quiz)}")
	print("\n📋 Detailed Results:")

	for i, (question, your_answer, correct_answer, is_correct) in enumerate(results, start=1):
		status = " Correct" if is_correct else " Incorrect"
		print(f"\n{i}. {question}")
		print(f"   Your answer: {your_answer}")
		print(f"   Correct answer: {correct_answer}")
		print(f"   Result: {status}")

def thank_you_ascii_art():
    art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠴⠶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⠉⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣴⣶⣶⣶⣶⣶⣤⣤⣄⣀⣀⡀⢀⣴⡿⠋⠀⠀⢀⡀⠰⣾⣆⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⢠⣤⣀⠀⠀⠀⠀⠀⠀
⢀⣴⠛⠉⠀⠀⠀⠀⠀⠈⠉⠉⢉⣿⠟⢻⣿⡿⠿⠿⠿⠟⠋⠀⠀⠙⠿⣷⣤⣀⡀⠀⣀⣤⠿⠃⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀
⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠋⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠉⠉⠁⠀⠀⣰⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣧⡀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠇⢠⣿⠋⣀⣤⡀⠀⠀⢀⣀⣀⣀⡀⠀⢀⣤⡄⢀⣠⣤⡄⠀⣰⣿⠋⣠⣶⣶⡄⠀⠀⠀⠀⠀
⠀⠻⠿⣿⣶⠀⠀⠀⠀⣰⣿⡏⢠⣿⣷⣾⣿⡿⠃⣠⣾⠟⢉⣿⡟⢁⣴⠟⣽⣿⠟⣹⣿⠇⣰⣿⣿⣟⣁⣴⡿⠁⠀⠀⠀⠀⣄
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⢀⣿⡿⠋⣾⡟⢁⣴⣿⣋⣠⣿⡏⣰⡿⢁⣼⡿⠃⢠⣿⣧⣾⣿⡿⢻⣿⡉⠁⠀⠀⠀⠀⠀⢻⣿
⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠀⠈⠻⠁⠀⠿⠿⠛⠙⠻⠛⠁⠻⠟⠋⠀⠈⠛⠁⠀⠘⠿⠛⠹⣿⠁⠀⠻⣿⣄⠀⠀⠀⠀⠀⢸⣿
⠀⣠⡀⠀⠀⠀⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣄⡀⢀⣠⡿⠃
⢸⡟⠁⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⢠⣿⠟⣠⣴⡾⣿⣿⠂⠀⣤⣤⠆⠀⣤⣤⡆⠀⠀⠀⠀⠈⠉⠛⠋⠉⠀⠀
⠘⠷⠤⠴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⣴⣿⣟⣼⡿⠋⢰⣿⣿⢃⣾⡿⠁⢀⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⢠⣾⣿⡏⢸⣿⠁⠀⣼⣿⠟⣿⡟⠀⣰⣿⡿⠁⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠻⠿⢫⣿⠟⠀⠸⣿⣴⣾⠟⠁⠀⠻⣷⠟⠋⢸⡇⠀⢀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠟⠛⠉⠛⠛⠛⠿⠿⣿⣶⣶⣤⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣿⠛⠿⢿⣷⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣷⡄⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠀⠀⠉⠙⠛⠻⠿⣶⣶⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⢀⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣉⣛⠓⠒⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⣤⠚⠉⣨⣽⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⠖⠋⣉⣩⣿⣿⡉⠀⠀⠀⠀⣾⣅⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢀⡼⡿⢷⡲⢤⣉⢙⣳⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣾⣿⣿⣧⣶⣋⣡⡟⣸⡇⠙⠶⣄⡀⠀⣻⣿⢻⣶⣿⣿⣿⣿⣿⣿⣻⣯⢿⣟⢀⣠⠾⢻⣄⣤⣤⡻⣴⣮⣙⢿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣈⠙⡒⠚⠳⡘⠛⠛⠿⢿⡿⠿⠛⠻⢿⠄⠀⣉⠁⣴⣿⣿⣿⣿⣿⣟⣿⣿⣶⣿⡟⠛⠛⠻⣧⡀⠀⠀⠀⠀⠀⠀
⡼⠋⠀⠀⠀⠉⠉⠉⠻⠿⠿⢿⣿⣿⣿⣿⡿⣿⠏⠁⠀⣿⣤⣠⡴⡾⢷⣤⣤⣤⣾⡃⠀⠉⠛⠻⣿⣿⣿⡿⠛⠉⠙⠁⠀⠀⠀⠀⠀⠀⠈⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠟⠁⠀⠀⠀⠺⡟⢻⣦⡍⠁⢀⠘⣷⡄⠛⠿⢿⠋⠀⠀⠀⠀⠙⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢨⡈⠉⣷⣶⣭⣿⣿⣾⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠈⠻⠛⠟⠛⠈⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣾⣻⣿⣿⣿⣿⣟⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠚⠿⢿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(art)


# Main program
# Main program
if __name__ == "__main__":
	filename = input("Enter the quiz filename (e.g., quiz.txt): ").strip()
	quiz_data = load_quiz(filename)

	if quiz_data:
		run_quiz(quiz_data)
	else:
		print("No data found in the quiz file.")

	thank_you_ascii_art()