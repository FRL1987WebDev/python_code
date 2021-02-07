print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
joined_names = name1 + name2
joined_names_lower = joined_names.lower()

t = joined_names_lower.count("t")
r = joined_names_lower.count("r")
u = joined_names_lower.count("u")
e = joined_names_lower.count("e")

true = t + r + u + e

l = joined_names_lower.count("l")
o = joined_names_lower.count("o")
v = joined_names_lower.count("v")
e = joined_names_lower.count("e")

love = l + o + v + e

true_love = str(true) + str(love)
true_love = int(true_love)

if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <=50:
  print(f"Your score is {true_love}, you are alright together.")  
else:
  print(f"Your score is {true_love}.")