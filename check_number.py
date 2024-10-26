def check_number():

    while True:
        try:
            guess_number = int(input("Необхідно вгадати ціле число від 1 до 100: "))
            if 1 <= guess_number <= 100:
                return guess_number
            else:
                print("Введене значення повинно бути більше 0 і не більше 100")

        except ValueError:
            print("Будь ласка, введіть коректне числове значення")