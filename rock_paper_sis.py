import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_turn = input("rock, paper, scissors?")

ai_turn = random.randint(1,3)

if player_turn == "rock":
  player_turn = rock
  print(rock)
elif player_turn == "paper":
  player_turn = paper
  print(paper)
elif player_turn == "scissors":
  player_turn = scissors
  print(scissors)  
else:
  player_turn = input("rock, paper, scissors?")  

if ai_turn == 1:
  ai_turn = rock
  print(rock)
elif ai_turn == 2:
  ai_turn = paper
  print(paper)
else:
  ai_turn = scissors
  print(scissors)

if player_turn == rock and ai_turn == rock:
  print("Its a draw!") 
elif player_turn == paper and ai_turn == paper:
  print("Its a draw!")
elif player_turn == scissors and ai_turn == scissors:
  print("Its a draw!")
elif player_turn == rock and ai_turn == paper:
  print("You lose!")
elif player_turn == rock and ai_turn == scissors:
  print("You win!")
elif player_turn == paper and ai_turn == rock:
  print("You win!")
elif player_turn == paper and ai_turn == scissors:
  print("You lose!")
elif player_turn == scissors and ai_turn == rock:
  print("You lose!")
elif player_turn == scissors and ai_turn == paper:
  print("You win!")
else:
  print("Start over!")     