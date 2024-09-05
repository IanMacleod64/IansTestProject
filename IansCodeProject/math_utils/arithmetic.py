import re
import pyinputplus as pyip
def addition_tool():
    numbers= re.compile(r'\d+')
    print('Please give numbers that should be added.')
    response = input()
    total_numbers = numbers.findall(response)
    print('I will be adding:' + str(total_numbers))
    for i, digit in enumerate(total_numbers):
        total_numbers[i] = int(digit)
    print('The sum of the provided numbers is ' + str(sum(total_numbers)))

def multiplication_tool():
    numbers= re.compile(r'\d+')
    print('Please give numbers that should be multiplied.')
    response = input()
    total_numbers = numbers.findall(response)
    print('I will be multiplying:' + str(total_numbers))
    for i, digit in enumerate(total_numbers):
        total_numbers[i] = int(digit)
    current = 1
    gs = 0
    for i in range(len(total_numbers)):
        current *= total_numbers[gs]
        gs += 1
    print('The multiplied total of the provided numbers is ' + str(current))

def subtraction_tool():
    numbers= re.compile(r'\d+')
    print('Please give the number you would like the future numbers to be subract from.')
    large = input()
    print('Please give the numbers you would like to subtract ' + str(large) + ' by.')
    response = input()
    total_numbers = numbers.findall(response)
    print('I will be subtracting ' + str(large) + ' by:' + str(total_numbers))
    for i, digit in enumerate(total_numbers):
        total_numbers[i] = int(digit)
    current = large
    gs = 0
    for i in range(len(total_numbers)):
        current = int(current) - total_numbers[gs]
        gs += 1
    print('The subtracted total of the provided numbers is ' + str(current))

def division_tool():
    numbers= re.compile(r'\d+')
    print('Please give the number you would like the future numbers to divide.')
    large = input()
    print('Please give the numbers you would like to divide ' + str(large) + ' by.')
    response = input()
    total_numbers = numbers.findall(response)
    print('I will be dividing ' + str(large) + ' by:' + str(total_numbers))
    for i, digit in enumerate(total_numbers):
        total_numbers[i] = int(digit)
    current = large
    gs = 0
    for i in range(len(total_numbers)):
        current = int(current) / total_numbers[gs]
        gs += 1
    print('The divided total of the provided numbers is ' + str(current))
