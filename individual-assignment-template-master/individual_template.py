#!/usr/bin/env python

"""
File: template.py
Name: Josh Smith

Description: Template file to be issued for each individual assignment
Sources: https://www.python.org/
"""

import random
import math

PI = 3.14


# Main function that will run when the file is executed
def main():
	a = random.randint(1,10)
	b = random.randint(1,10)
	c = random.randint(10,20)
	
	result1 = pythagorean(a, b)
	result2 = circumference(c)
	result3 = area(a, b, c)
	
	print("Pythagorean's Theorem of {a}m and {b}m: {result1}m".format(a=a, b=b, result1=result1))
	print("Circumference of a circle with a radius of {c}m: {result2}".format(c=c, result2=result2))
	print("Area of a rectangle with dimmensions {a}mx{b}mx{c}m: {result3}m".format(a=a, b=b, c=c, result3=result3))
	
	
# Returns the hypotenuse of a triangle
# Parameters: num1 (number, side length of the first line), num2 (number, side length of the second line)
def pythagorean(num1, num2):
	return math.sqrt(num1**2 + num2**2)
	
	
# Returns the circumference of a circle
# Parameters: radius (raduis of the circle)
def circumference(radius):
	return 2 * PI * radius
	

# Returns the area of a rectangle
# Parameters: length (number), width (number), height (number)
def area(length, width, height):
	return length * width * height
	
	
if __name__ == "__main__":
	main()
