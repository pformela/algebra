import cmath
import os

additionStr = "1. Dodawanie"
multiplicationStr = "2. Mnożenie"
divisionStr = "3. Dzielenie"

def show_menu():
    os.system("clear")
    print("Kalkulator liczb zespolonych".center(40, "#") + "\n")
    print("Wybierz działanie:")
    print(additionStr.rjust(len(additionStr) + 5, " "))
    print(multiplicationStr.rjust(len(multiplicationStr) + 5, " "))
    print(divisionStr.rjust(len(divisionStr) + 5, " ") + "\n")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b;


def main():

    show_menu()
    operations = [add, multiply, divide]

    while True:

        numbers = []

        while True:
            try:
                operation = int(input("Wprowadź numer działania: "))
                if operation not in [1, 2, 3]:
                    raise Exception("Wprowadzono złe dane")
            except:
                show_menu()
                print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
            else:
                break

        while True:
            try:
                amount_of_numbers = int(input("Wprowadź ilość liczb: "))
            except:
                print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
            else:
                break

        while True:
            try:
                number = int(input("Wprowadź liczbę: "))
                numbers.add(number)
            except:
                print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
            else:
                break

        

    

if __name__ == "__main__":
    main()
