# Hang Man
The goal of this program is to create hangman on the computer 
## Sample input ## 
    >>The anwser is a 5 letter word
    >>You have 5 lives remaining
    >>Guess a letter: h
    >>Correct! 
    >>h _ _ _ _
    > >>You have 5 lives remaining
    >>Guess a letter: a
    >>Incorrect
    >>You have 4 lives remaning. 
    >>Guess a letter:p
    >>Correct! 
    >>h _ p _ _
    >>You have 4 lives remaining
    ......
    >>You Won! 
## Reference ##
This progam is tricky so here are some hints to help you get through
### len ###
Gives you length of a string
  
    name= "Yasas"
    print(len(name))
    >>5
### subString in string ###
returns true if a substring is in a string 

    name="Yasas"
    "y" in name ---> True
    "b" in name ---> False 
    "asa" in name ---> True
    
### end="" ###
Used to print without going to a new line. 
    
     print("Hello ", end="")
     print (" World")
     

