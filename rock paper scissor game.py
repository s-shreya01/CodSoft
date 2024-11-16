import random

user_score=0
computer_score=0
rounds=5

choice=['rock','paper','scissor']
for i in range(rounds):
    user_choice=input("enter choice:")
    comp_choice=random.choice(choice)
    print("comp_choice:",comp_choice)

    if user_choice == comp_choice:
        print("it's a tie!")
    elif(user_choice=='rock'and comp_choice=='scissors',
         user_choice=='paper' and comp_choice=='rock',
         user_choice=='scissors' and comp_choice=='paper'):
      print("user win!")
      user_score+=1
    else:
     print("comp_wins!")
     computer_score+=1

print(f"Final score-user:{user_score} computer:{computer_score}")


    