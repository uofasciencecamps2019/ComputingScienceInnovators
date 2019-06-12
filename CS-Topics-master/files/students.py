#!/usr/bin/env python3

"""
File: students.py
Name:

Description:
Sources:

===============================================
Template on how to open and read a file
===============================================
file = open(filename)	# Opens the file and stores the file object in <file>
file_contents = []		# Creates a list to store the lines in the file

for line in file.readlines():	# Goes over each line in the file
    file.contents.append(line)	# Appends each line in the file to <file_contents>
    
file.close()	# Closes the file, since we are now done with the file
				# We still have access to all the lines in the file, since we stored them in <file_contents>
===============================================
"""


def main():
    filename = "data.txt"
    students = {}

    populate_dicts(students, filename)
    add_letter_grades(students, letters_added)
    display_students(students)


# This will add the student data from the file into the dictinoary that was initiailzed in the main() function
def populate_dicts(students, filename):
    datafile = open(filename)

    for line in datafile.readlines():
        cleaned = line.rstrip().split(',')
        id_number, grade = "".join(cleaned[1].split()), eval("".join(cleaned[2].split()))
        
        students[cleaned[0]] = [id_number, grade]

    datafile.close()


# This will add the letter grades to the end of the dictionary keys
def add_letter_grades(students, letters_added):
    # Code here


# This will print all of the student data (names, IDs, grades)
def display_students(students):
    # Code here


if __name__ == "__main__":
    main()
