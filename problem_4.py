#!/usr/bin/env python3
import math
import csv
from math import sqrt

class Shape:

    def __init__(self, length):

        self.length = float(length)


    # Calculate area and perimeter of a triangle and return both as string
    def triangle(self):

        self.area = round((math.sqrt(3)/ 4)*(self.length * self.length), 2)

        self.perimeter = self.length *3

        return f"A triangle with side length {self.length} u has a perimeter of {self.perimeter} u and area of {self.area} u^2"

    # Calculate area and perimeter of a square and return both as string
    def square(self):


        self.shape = 'square'

        self.area = round(self.length * self.length, 2)

        self.perimeter  = self.length*4

        return f"A {self.shape} with side length {self.length} u has a perimeter of {self.perimeter} u and area of {self.area} u^2."

    # Calculate arem and perimeter of a circle and return both as string
    def circle(self):


        self.shape = "circle"

        self.area = round(math.pi * self.length * self.length, 2)

        self.perimeter = round(2 * math.pi * self.length, 2)

        return f"A {self.shape} with radius {self.length} u has a radius of {self.perimeter} u and area of {self.area} u^2."

    # Calculate area and perimeter of a pentagon and return both as string
    def pentagon(self):

        self.shape = "pentagon"

        self.area = round((sqrt(5 * (5 + 2 *
           (sqrt(5)))) * self.length * self.length) / 4, 2)

        self.perimeter = self.length * 5

        return f"A {self.shape} with side lenght {self.length} u has a perimeter of {self.perimeter} u and area of {self.area} u^2."


def main():


    # open csv file
    with open("test_file.csv") as csv_file:

        # read file
        csv_reader = csv.reader(csv_file, delimiter=',')

        # travers file row by row
        for row in csv_reader:

            # if shape in row then run Shape() class instance and print the return string
            if row[0] == 'triangle':

                triangle = Shape(row[1])
                print(triangle.triangle())

            elif row[0] == 'square':

                 square = Shape(row[1])
                 print(square.square())

            elif row[0] == 'circle':

                circle = Shape(row[1])
                print(circle.circle())

            elif row[0] == 'pentagon':

                pentagon = Shape(row[1])
                print(pentagon.pentagon())


if __name__ == '__main__':
    main()
