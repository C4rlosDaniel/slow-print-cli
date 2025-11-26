import os
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def process_answer(answer, name):
    os.system('cls' if os.name == 'nt' else 'clear')

    if answer == '1':
        slow_print(f"\n{name}, life gains purpose when you create one.")
        slow_print("Every choice you make builds your path. \n")

    elif answer == '2':
        slow_print(f"\n{name}, freedom begins when you take control of your own story.")
        slow_print("And that starts with small actions every day.\n")

    elif answer == '3':
        slow_print("\nWhat truly matters are the connections, the experiences, and the impact you leave behind.")
        slow_print("And, of course, how you use your time.\n")

    elif answer == '4':
        slow_print("\nSometimes wasting time isn't bad… as long as it's with something that makes you feel good. \n")

    elif answer == '0':
        slow_print("\nSee you next time! \n")
        exit()

    else:
        slow_print("❗ Please choose only between 0, 1, 2, 3, or 4.\n")

def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    slow_print("Hello! Welcome back!")
    name = input("Enter your name: ").strip()
    email = input("Enter your best email: ").strip()

    slow_print(f"\nPerfect, {name}! Let's begin...\n")

    while True:
        slow_print("What would you like to know today?")
        print("[1] What is the true purpose of life?")
        print("[2] Do you want to be free?")
        print("[3] What really matters?")
        print("[4] Just want to pass the time?")
        print("[0] Exit")
        
        answer = input("\nChoose an option: ").strip()
        process_answer(answer, name)

start()
