import math
import random

def calculate_z(n, m):
    z = (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)
    return z

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

    break

z = calculate_z(n, m)
print(f"Значення Z дорівнює {z}")

def guessing_number():
    number = random.randint(1, 100)
    print(f"ПІДКАЗКА. Згенероване число дорівнює {number}")
    while True:
        try:
            guess_number = int(input("Необхідно вгадати число від 1 до 100: "))
            if guess_number <= 0 or guess_number > 100:
                print("Введіть значення від 1 до 100")
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
