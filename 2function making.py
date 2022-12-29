"""Developed by Orlando Companioni
Date:October 13 2022

using functions with modular addition
"""
#input function 
def useInput():      
    userInput=int(input("Enter a number: "))
    return userInput         #returns the value of user input

#does the calculations using the input gathered
def calProcess(val):
    value=val**2      #it works, just return value
    return value      #returns the value of the calculation


#outputs the answer
def output(answer):                 
    
    print(f"The answer is: {answer}")

def main():
    num=useInput()
    square=calProcess(num)
    output(square)    #calling the output function to output the answer

main() #calling the main function
    
    
