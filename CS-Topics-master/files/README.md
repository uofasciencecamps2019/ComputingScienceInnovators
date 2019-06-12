# File IO Assignment

### Task
1. Download **both** the students.py file and the data.txt file above
2. Complete the tasks outlined by each of the functions and comments in the students.py file

### Rules
1. Asking your peers for help is okay, but try not to copy and paste their code
2. If you get any code from peers or online sources, cite your sources
3. Make sure your code is compatible with Python3 (some things you look up will work for Python2 but not Python3)

**General rule of thumb:** If you can explain your code in your own words, that proves that you can understand it


### Code formatting
An example has been provided in this repository and is linked [here](https://github.com/UofAScienceCamps2018/CS-Topics/blob/master/files/students.py)


```python
#!/usr/bin/env python3

"""
File: students.py
Name:

Description:
Sources:
"""


def main():
    filename = "data.txt"
    students = {}

    populate_dicts(students, filename)
    add_letter_grades(students, letters_added)
    display_students(students)


# This will add the student data from the file into the dictinoary that was initiailzed in the main() function
def populate_dicts(students, filename):
    # Code here


# This will add the letter grades to the end of the dictionary keys
def add_letter_grades(students, letters_added):
    # Code here


# This will print all of the student data (names, IDs, grades)
def display_students(students):
    # Code here


if __name__ == "__main__":
    main()
```