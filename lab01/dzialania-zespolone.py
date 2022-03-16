import cmath
import os

additionStr = "1. Dodawanie"
multiplicationStr = "2. Mnożenie"
divisionStr = "3. Dzielenie"

def show_menu():
    os.system("clear")
    print(" Kalkulator liczb zespolonych ".center(40, "#") + "\n")
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

    operations = [add, multiply, divide]

    while True:

        show_menu()

        numbers = []
        amount_of_numbers = 0
        result = complex(0, 0)
        nextOperation = "t"

        # Wybór działania
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

        # Wprowadzenie ilości liczb
        if operation != 3:
            while True:
                try:
                    amount_of_numbers = int(input("Wprowadź ilość liczb: "))
                    if amount_of_numbers <= 0:
                        raise Exception("Wprowadzono złe dane")
                except:
                    show_menu()
                    print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
                else:
                    break
        else:
            amount_of_numbers = 2

        # Wprowadzenie liczb
        while amount_of_numbers >= 1:
            try:
                number = complex(input("Wprowadź liczbę w formacie(\"n+mj\", gdzie n i m to liczby rzeczywiste): "))
            except:
                print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
            else:
                numbers.append(number)
                amount_of_numbers -= 1

        # Obliczenie wyniku
        if len(numbers) == 1:
            result = numbers[0]

        if len(numbers) >= 2 :
            result = operations[operation-1](numbers[0], numbers[1])
            for i in range(2, len(numbers)):           
                result = operations[operation-1](result, numbers[i])

        print("Wynik to: " + str(result))

        # Kontynuacja obliczeń
        while True:
            try:
                nextOperation = str(input("Czy chcesz kontynuować (t/n)? "))
                if nextOperation not in ["t", "n", "T", "N"]:
                    raise Exception("Wprowadzono złe dane")
            except:
                print("Wprowadzono błędne dane. Spróbuj jeszcze raz.")
            else:
                break

        if nextOperation.lower() == "n":
            break 

if __name__ == "__main__":
    main()
