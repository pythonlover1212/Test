#EXTRA NOTES I FORGOT:
#To make comments, put a "#" at the start of the line of code. This is good for debugging/ making notes so that the future you doesnt forget what that line of code means
# A variable is a character (a-z) to represent a something else. (x = 7, y = 15, "pizza" etc.)
#A string is a sentence/words wraped around quotation marks " ". 
#An interger is a whole number
#Intergers and strings are completely different. 7 and "7" are completely different things.

import random
#random is an internal moduel in python. There are various modules inside python but this one allows the program to generate random numbers

def guess(x):
#This is a function. A function is basically a block a code you can "call" when needed. 

    computer_number = random.randint(1,100)
    #This is me using the random module to create an interger that will be stored in the program. The 1 is the first number in the range and the 100 is the last number in the range. This is the number the player will have to guess. 
    
    while computer_number >= 1 and computer_number<= 100:
    #This is a while loop. A while loop can be use to keep a program going while a certain condition is met. In this example, the condition that is met is the random number that the computer generated on line 7.    
        
        x = input("Type in your number:")
        #This is how you get the user's input. You declare a variable (in this case x) and you type "input("put your question/ text here")"
        
    
        x = int(x)      
        #This is casting. When you ask for the user input, the computer automatically takes the input as a string. We need to change this back into an interger for python to understand that the number we are inputting will be the number that the computer generated.
        
        if x == computer_number:
        #This is an if statement. If statements are only executed when the condition on the left is met.     
            print("Correct! The number was " + str(computer_number))
            #The str() is another example of casting but in this case, we are casting the interger into a string. While printing, your statement must be all numbers/ or all strings
            
            break
            #You use the word "break" to exit the loop.
    
        while x != computer_number:
        #Another while loop. The symbol != means "Does not"
            if x > computer_number:
        
                print("Incorrect! That's too high!")
            
                break
            
            elif x < computer_number:
            
                print("Incorrect! That's too low!")
            
                break
            

            

print("I am thinking of a number 1-100, and I want you to guess what number that is. Guess as many times as you need to in order to get to the number I am thinking of.\n")    
guess(input)
#I call the block of code I made between line 11 and 47.
     