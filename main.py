import random
import time

min_value = 1
max_value = 6

max_value_answer = input("How many sides should the dice have? (default = 6) ")

if max_value_answer!= "" and max_value_answer.isnumeric():
    max_value = int(max_value_answer)

def rolling_dice():
    return random.randint(min_value, max_value)

def loading():
    print("Dolling dice: ")
    time.sleep(0.5)

while True:
    answer = input("Shall we roll the dice? [y/n] ")

    if answer == "y":
        loading()
        print(rolling_dice())
    elif answer =="n":
        print("Bye...")
        break
    else:
        print("Invalid response! [y/n] ")
