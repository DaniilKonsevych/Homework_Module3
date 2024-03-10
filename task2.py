import random

def get_numbers_ticket(min : int, max : int, quantity : int):

    #Перевірка значень
        
    if min > max:
        reverse_min = max
        reverse_max = min
        max = reverse_max
        min =  reverse_min
        print("Minimum and Maximum were reversed.")

    if type(min) != int:
        min = 1
        print("When calling the function, minimum wasn't an integer. Minimum set to 1")
    elif min < 1:
        min = 1
        print("When calling the function, minimum was set below 1. Setting minimum to 1.")

    if type(max) != int:
        max = 1000
        print("When calling the function, maximum wasn't an integer. Maximum set to 1000")
    elif max > 1000:
        max = 1000
        print("When calling the function, maximum was set above 1000. Setting maximum to 1000.")

    if type(quantity) != int:
        quantity = 1
        print("When calling the function, quantity of numbers wasn't an integer. Quantity of numbers set to 1")
    elif quantity < 1:
        quantity = 1
        print("When calling the function, amount of unique numbers was set below 1. Setting amount of unique numbers to 1.")
    elif quantity > max:
        quantity = max - 1
        print("Too many unique numbers requested when calling the function. Quantity of unique numbers was set to max - 1.")

    #Поверненя значень
    return random.sample(range(min, max), quantity)

#Тестування
print(get_numbers_ticket(1, 50, 5))
print(get_numbers_ticket(0, 50, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(2, 50, -1))
print(get_numbers_ticket("ф", "50", ";"))
print(get_numbers_ticket(50, 1, 5))
print(get_numbers_ticket(1, 50, 51))
