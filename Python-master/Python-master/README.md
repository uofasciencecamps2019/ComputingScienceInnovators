# Python-Assignments
## Reference ##
#### `print` ####
You will use this command to display messages to the user. `print("Hello World")` 

    name = "Yasas"
    print("Hello "+ name)
#### `input` ####
This command is used to take in user inputs. `input("Please enter your name")`

    name = input("Please enter your name")

#### Data types ####
Python has many different data types some of the main ones are:

String(`str`)   Integer(`int`)   Float(`float`)  Boolean(`bool`)

To convert between data types, use the following:

    num=int(numberString)
#### Logic ####
Logical operators and conditional statements are used by the computer to make decisions. 

       if (name=="Yasas"):
            ....
        elif(name="Tem"):
            ....
        else:
            ....
The operators `and`, `or` can also be used. 
#### Random ####
To generate random number, we must import a module called random. 

    import random
    rand_I=random.randint(min,max)
 
#### Lists ####
Lists are used to store multiple pieces of information of the same type in a single variable with with different indices. 

The following is an example using a list:

    fruits = ["Apple","Orange", "Pear"]
    print(fruits[0])
    print(fruits[2])
    fruits.append("Banana")
    
#### Loops ####
`for` loops and `while` loops are used to repeat a section of code multiple times.

For Loop: 

    for fruit in fruits:
        print(fruits)
        
While Loop:
    
    condition=True 
    while (conditon):
        if input("Type 'q' to exit ")=="q":
            condition=False 
##### `Range` #####
Useful in for loops when you need it to iterate with numerical values. range(upper_Limit,lower_Limit).

    for num in range(1,5):
        print("Player " + str(num))
    >>Player 1
    >>Player 2
    >>Player 3
    >>Player 4
    >>Player 5
              
#### Function ####
Functions are a set of instructions that can be used multiple times through out a program. They are given values and can return values. 

    def cube(inputValues):
        ans=iinputValues*inputValues*inputValues
        return ans
    number = int(input("Enter a number to cube "))
    anwser = cube(number)
    print(anwser)
        
