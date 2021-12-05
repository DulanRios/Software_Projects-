"""This is my integration project COP 1500 2021"""
__author__ = "Dulan Rios-Lopez"

import math


# function to begin the program/project

def main():
    """Calls to start the program and introduce the user with a menu """
    print("Welcome to my Integration Project")
    resume_program = True
    # loops when the user picks an option
    while resume_program:
        print("Here are your different options")
        print("1. Area of a square")
        print("2. Addition")
        print("3. Subtraction")
        print("4. Returning a list")
        print("5. Area of a Circle")
        print("6. Exit")
        user_1 = int(input())
        if user_1 == 1:

            while True:
                try:
                    side = int(input("Enter the side of the square: "))
                    break
                except ValueError:
                    print("Error. Input must be a whole number! ")
            print(area_of_square(side))

        elif user_1 == 2:
            while True:
                try:
                    num3 = int(input("Please enter the first number: "))
                    num4 = int(input("Please enter the second number: "))
                    break
                except ValueError:
                    print("Error. Input must be a whole number! ")
            print(get_addition(num3, num4))

        elif user_1 == 3:
            while True:
                try:
                    num1 = int(input("Please Enter the first number: "))
                    num2 = int(input("Please Enter the second number: "))
                    break
                except ValueError:
                    print("Error. Input must be a whole number! ")
            print(get_subtraction(num1, num2))

        elif user_1 == 4:
            print(input("This creates a list for numbers between 0 and 9 "))
            numbers = create_list()
            print(numbers)
            create_list()
        elif user_1 == 5:
            circleArea()
        elif user_1 == 6:
            resume_program = False
            # if user enters 6 or anything more than 6 the program quits
            print("Have a good day!")
        else:

            print("Invalid selection. Please try again.")


# Finding area of a square using a function
def area_of_square(side):
    """Finds the area of the square from the user entering one side of the
    square"""

    return side * side


# function to create a list from the numbers 0-9
def create_list():  # function definition for returning a list
    """Function to return list"""
    return [i for i in range(10)]


# function to configure the sum from the user inputs
def get_addition(num3, num4):  # function definition for addition
    """Asks the user to input two numbers and the function solves for the
    sum """
    total = num3 + num4

    return total


# python program to calculate the area of a circle giving the radius
def calcArea(radius):  # function definition for radius
    """Calculates the Area with the radius"""

    area1 = math.pi * radius ** 2
    print("Area with radius of", radius, "is", format(area1, ".2f"))


def circleArea():
    """returns radius"""
    radius = float(input("Please enter the radius: "))
    calcArea(radius)


# python program to subtract two numbers using a function
# function definition for subtraction

def get_subtraction(num1, num2):
    """ Asks the user to input two numbers and the function solves the
    difference."""

    difference = num1 - num2
    return difference


if __name__ == '__main__':
    main()
