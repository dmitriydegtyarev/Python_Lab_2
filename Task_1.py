import math
import random

def calculate_z(n, m):
    return (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)

def check_input_and_calculate_z ():
    while True:
        try:
            n = float(input("Введіть значення n: "))
            m = float(input("Введіть значення m: "))
        except ValueError:
            print("Будь ласка, введіть коректне числове значення")
            continue

        if m == 0:
            print("Значення змінної m не може дорівнювати 0")
            continue

        z = calculate_z(n, m)
        print(f"Значення Z дорівнює {z}")
        break

check_input_and_calculate_z ()

def guessing_number():
    number = random.randint(1, 100)
    print(f"ПІДКАЗКА !!! =>>>> {number} є загадане число")
    while True:
        try:
            guess_number = int(input("Необхідно вгадати ціле число від 1 до 100: "))
            if guess_number <= 0 or guess_number > 100:
                print("Введене значення повинно бути більше 0 і не більше 100")
            elif guess_number < number:
                print("Моє число більше")
            elif guess_number > number:
                print("Моє число менше")
            else:
                print("Ви вгадали!")
                break
        except ValueError:
            print("Будь ласка, введіть коректне числове значення")

guessing_number()