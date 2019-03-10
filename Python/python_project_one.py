###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly

import random

def random_digit():
  digits = [str(num) for num in range(10)]
  random.shuffle(digits)
  return digits[:3]

def check_win(choice,num):
  return choice == num

def check_match(choice,num):
  for ind,dig in enumerate(choice):
    return dig == num[ind]

def check_close(choice,num):
  for dig in choice:
    return dig in num

play_num = random_digit()
print(play_num)

guessed = False

while guessed != True:

  user_choice = list(input("Enter a 3 digit number: "))

  if check_win(user_choice,play_num):
    print("Your guess was correct!")
    guessed = True
  elif check_match(user_choice,play_num):
    print("Match: You've guessed a correct number in the correct position")
  elif check_close(user_choice,play_num):
    print("Close: You've guessed a correct number but in the wrong position")
  else:
    print("Nope: You haven't guessed any of the numbers correctly")



