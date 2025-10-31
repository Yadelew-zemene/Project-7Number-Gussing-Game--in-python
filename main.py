"""
NUber gussing game for players
"""
print("""
Well come to NUmber Guessing Game
 Good lack!!""")
from random import randint
print("Let me think a number between 1 and 50")
num_generated=randint(1,50)
Game_level=input("choose the level hard/easy").lower()
num_guess=10
option ="yes"
while option=='yes':
    num_generated = randint(1, 50)
    Game_level = input("choose the level hard/easy").lower()
    num_guess = 10
    if Game_level=="easy":
      print("you have 10 attempts for easy game")
      while num_guess>0:
        uesr_num=int(input("Make a Guess"))
        if uesr_num not in range(1,50):
            print("Wrong number. Please Enter in range 1 to 50!")
        elif uesr_num>num_generated:
            print("Your guess is Too high")
            num_guess-=1
            print(f"You have only {num_guess} attempts!")
        elif uesr_num < num_generated:
            print("Your guess is Too Low")
            num_guess -= 1
            print(f"You have only {num_guess} attempts!")
        elif uesr_num==num_guess:
            print("congratulation. You win!!")
            break


    elif Game_level=="hard":
      num_guess=5
      print("you have 5 attempts for easy game")
      while num_guess > 0:

         uesr_num = int(input("Make a Guess"))
         if uesr_num not in range (1, 51):
            print("Wrong number. Please Enter in range 1 to 50!")


         elif uesr_num> num_generated:
            print("Your guess is Too high")
            num_guess-=1

            print(f"You have only {num_guess} attempts!")
         elif uesr_num < num_generated:
            print("Your guess is Too Low")
            print(f"You have only {num_guess} attempts!")
            num_guess-=1
         elif uesr_num == num_guess:
             print("congratulation. You win!!")
             break

    option=input("Do you Want to play again yes/no").lower()











