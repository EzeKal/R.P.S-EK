# Made by Ezel K. A rock, paper, scissors app for tablets, phones, computers & other devices able to run the Python coding language in a terminal.
# Read the file labelled 'rpsMulti_description.txt' in this repo to learn how to use this app and install this app onto your device.
# Copyright (C) 2026 Ezel K.
# Licensed under the MIT License (see LICENSE file).

import random
from time import sleep

game = True
user = 0
robot = 0
win = '\n       |\n      |\n     |\n|   |\n | |\n  |\n'
lose = '\n|     |\n |   |\n  | |\n   |\n  | |\n |   |\n|     |\n'
tie = '\n   --------\n'

while game:
  print(3)
  sleep(0.75)
  print(2)
  sleep(0.75)
  print(1)
  sleep(0.75)
  
  user = input("\nLet's go!!! To start playing, choose your option. Type the word 'rock' , 'paper' or 'scissors' , then press enter.\n\nEnter your option here ---> ")
  
  robot=random.randint(1,3)
  
  if user == 'rock':
    if robot == 1:
      sleep(0.75)
      print(tie)
      print("Robot chooses rock, it's a tie!")
    elif robot == 2:
      sleep(0.75)
      print(lose)
      print("Robot chooses paper, you lose!")
    elif robot == 3:
      sleep(0.75)
      print(win)
      print("Robot chooses scissors, you win!")
  elif user == 'paper':
    if robot == 2:
      sleep(0.75)
      print(tie)
      print("Robot chooses paper, it's a tie!")
    elif robot == 3:
      sleep(0.75)
      print(lose)
      print("Robot chooses scissors, you lose!")
    elif robot == 1:
      sleep(0.75)
      print(win)
      print("Robot chooses rock, you win!")
  elif user == 'scissors':
    if robot == 2:
      sleep(0.75)
      print(win)
      print("Robot chooses paper, you win!")
    elif robot == 3:
      sleep(0.75)
      print(tie)
      print("Robot chooses scissors, it's a tie!")
    elif robot == 1:
      sleep(0.75)
      print(lose)
      print("Robot chooses rock, you lose!")
  sleep(0.25)
  status = input("\nDo you want to play another match? Type 'yes' or 'no''.\n\nEnter your option here ---> ")
  if status == 'no':
    game = False
