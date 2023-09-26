#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: September 26, 2023
# This program displays the area and perimeter of a rectangle with user input


def main():
    # get length and width
    print("Calculating the Area and Perimeter of a Rectangle")
    length = int(input("What is the length of your rectangle?"))
    width = int(input("What is the width of your rectangle?"))

    # calculate area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # display area and perimeter
    print("The area is {} cm^2".format(area))
    print("The perimeter {} cm".format(perimeter))


if __name__ == "__main__":
    main()
