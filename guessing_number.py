import random
from check_number import check_number

def guessing_number():
    number = random.randint(1, 100)
    print(f"ПІДКАЗКА. Згенероване число дорівнює {number}")
    while True:
        guess_number = check_number()
        if guess_number <= 0 or guess_number > 100:
            print("Введене значення повинно бути більше 0 і не більше 100")
            continue
        elif guess_number < number:
            print("Моє число більше")
            continue
        elif guess_number > number:
            print("Моє число менше")
            continue
        else:
            print("Ви вгадали!")
            break