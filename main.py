"""My Integration Project"""
__author__="Dulan Rios-Lopez"
# This project is a math quiz about calculating the area of triangles and
# classifying triangles
# Sources include w3schools.com, "Learn to Program" Derek Banas video
# playlist, and Think Python 2nd Edition Version 2.4.0
import math

# Ask the user for their name and print a greeting statement
name = input("Hi! What is your name? ")
print('Welcome, ' + name + ' to Dulans integration project!')

# State what the project is about
input("Today were going to take a math quiz involving triangles. Press enter"
      " to continue: ")

# Enter the first math question
print("1. Find the area of the triangle base= 5, height= 25")

# Allow user to input answer
area = eval(input("Enter your answer: "))
# Print Results
print(area)
# Congratulate user for correct answer
if area == 62.5:
    print("Correct!")
else:
    print("Incorrect!")

# Enter the second math question
print(
    "2. Find the area of the right triangle with a base of 5 and height of 8.")

# Receive area and store in area
area = eval(input("Enter your answer: "))

# Change 20.0 to from decimal to integer and set variables

print(float(area))

# Print the result


# If user inputs correct answer congratulate
if area == 22.5:
    print("Correct!")
else:
    print("incorrect")

# Enter the third math question
print("3. John created a triangle shaped garden. If the base is 1.4 and a "
      "height of 2.6, how much fertilizer will he need? ")

# Receive area and store in area
area = eval(input("Enter your answer: "))

# Set variables

float_str = float(area)

# Print the result
print(area)

# If user inputs correct answer congratulate
if area == 1.82:
    print("Correct!")
else:
    print("Incorrect")

# Enter the fourth math question
print("4. A triangle has a side lengths of 2 inches, 2 inches, and "
      "3.5 inches. Classify the triangle.")
print("A. Scalene\nB. Isosceles\nC. Equilateral\nD. Right Obtuse")

# let user put in an answer
triangle = (input("Enter your answer: "))

# Print results
print(triangle)

# If user inputs correct answer congratulate if wrong answer correct it
if triangle == str('B'):
    print("Correct!")
else:
    print("Incorrect!")

# Thank the user for playing
print('Thank you ' + name + ' for playing!')

# Integration project Sprint 2 Inspection
# sources - w3schools.com, pogils 10-14, Derek Banas videos,

input("↓ This is sprint 2 of the project. Press Enter to continue. ↓: ")


# Finding area of a square using a function
def area_of_square(side):
    return side * side


print("1. Enter the Side Length of Square: ", end="")
length = float(input())
a = area_of_square(length)
print("\nArea = {:.2f}".format(a))

# Using standard conditional structures/statements to find even/odd num in list
print(
    '\n2. Finding the even/odd numbers in the list [10, 13, 15, 100, 6, 3, 8, '
    ' 54, 39, 68] ')
list1 = [10, 13, 15, 100, 6, 3, 8, 54, 39, 68]
num1, num2 = 0, 0
# iterating each number in the list
for num in list1:
    if num % 2 == 0:
        num1 += 1
    else:
        num2 += 1
print("Even numbers in the list: ", num1)
print("Odd numbers in the list: ", num2)

import random

# Guessing game using while
num = random.randint(1, 20)
while True:
    print('\n3. Guess a number between 1 and 20 in less than six tries')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!')
        break
    elif i < num:
        print('Try Higher!')
    elif i > num:
        print('Try Lower!')
print('if you guessed less than 6 times you won!')

print('\n4. Outputs true if weight is less than 10 and cost is less than 20'
      ' otherwise, its false.')
weight = float(input("Enter weight: "))
cost = float(input("Enter cost: "))
if weight < 10 and cost <= 20.00:
    print("True")
else:
    print("False")

# calculates the amount owed
print('\n5. Enter the right amount of payment for the two items.')
first_item = float(input("Enter The price of the first item: "))
second_item = float(input("Enter The price of the second item: "))
total = first_item + second_item
payment = float(input("Enter amount of payment "))
if payment < total:
    print("You still owe = {:,.2f}.".format(total - payment))


else:
    print("Thank you. Your change is = {:.2f}".format(payment - total))

# prints the multiples of 100
# Having divided by n, having 0 as a remainder, are all multiples of n
input('\n6. Prints the multiples of 100 using range().')
# Having divided by n, having 0 as a remainder, are all multiples of n
multiplesOfNumber = [n for n in range(1, 101) if n % 5 == 0]
print(multiplesOfNumber)

input('\n7. Prints the name and age of Dulan Rios.')


# defining a name and age
def name_age(name1, age=20):
    print("Name:", name1)
    print("Age:", age)
    return


name_age(name1="Dulan")

# Returns a boolean stating whether two expressions are not equal
input('\n8. Returns a boolean stating whether two expressions are not equal'
      ' or equal.')
a = 1
b = 2
print("A is equal to B:", a != b)
# Returning a list using append()
input('\n9. Returning a list using append()')


def listReturned():
    list3 = []
    for y in range(0, 16):
        list3.append(y)
    return list3


retList = listReturned()
print(retList)

# Finding radius of circle (Help from pogil)
print('\n10. Finding Area of circle with Radius input')


def calcArea(radius):
    area1 = math.pi * radius ** 2
    print("Area with radius of", radius, "is", format(area1, ".2f"))


def main():

    radius = float(input("Please enter the radius: "))
    calcArea(radius)


main()
