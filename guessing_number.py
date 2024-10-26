import random

def guessing_number(guess_number):
    number = random.randint(1, 100)
    print(f"ПІДКАЗКА. Згенероване число дорівнює {number}")

    while True:
        if guess_number < number:
            print("Моє число більше")
        elif guess_number > number:
            print("Моє число менше")
        else:
            print("Ви вгадали!")
        break