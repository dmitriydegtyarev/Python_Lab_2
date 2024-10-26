def check_number():

    while True:
        try:
            guess_number = int(input("Необхідно вгадати число від 1 до 100: "))
            if 1 <= guess_number <= 100:
                return guess_number
            else:
                print("Необхідно ввести ціле число від 1 до 100")

        except ValueError:
            print("Будь ласка, введіть коректне числове значення")