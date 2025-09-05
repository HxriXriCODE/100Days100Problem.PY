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
import random

List=[rock,paper,scissors]
RobotChoice=random.randint(a=0 ,b=2)
process2=List[RobotChoice]
print("Welcome to Rock Paper Scissor")
UserChoice=int(input("Rock:0 ,Paper:1,Scissor:2 \n"))
process=List[UserChoice]
print(process2)
print(process)
if process==RobotChoice:
    print("Draw")
elif RobotChoice==0 and UserChoice ==2:
    print("Robot Won")
elif RobotChoice==1 and UserChoice==0:
    print("Robot Won")
elif RobotChoice==2 and UserChoice==1:
    print("Robot Won")
else:
    print("You Won ")

