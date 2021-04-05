import json
import random
import time
import os
def play():
	print("\n==========QUIZ START==========") 
	score = 0 
	with open("questions.json", 'r+') as f: 
		j = json.load(f) 
		for i in range(10): 
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option) 
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')
def rules():
	print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (not case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
	''')
def about():
	print('''\n==========ABOUT US==========
This project has been developed by
SL.N0-  NAME   ROLL NO.
 1)    AFTAB     1  
 2)    AMBER     2
 3)    ANIKET    3
 4)   SHADMAAN   31
Students of Class XII Science of Kendriya Vidyalaya, CHITTARAJAN.''')
if __name__ == "__main__":
	choice = 1
	while choice != 5:
		print('\n=========WELCOME TO MIND CRUSHER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
		print('3. ABOUT US')
		print('4. EXIT')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			rules()
		elif choice == 3:
			
			about()
			
		elif choice == 4:
			time.sleep(3)			
			print('HOPE YOU ENJOYED OUR GAME. SEE YOU SOON')
			break
			os._quit()
			
		else:
			print('INVALID INPUT. TRY AGAIN!')
			continue
