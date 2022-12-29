'''
Developed by Orlando Companioni
Date november 3 2022

calculates x**y
'''
def main():
    number1=int(input("enter a number"))    #asking input
    number2=int(input("enter a second number"))
    answer=power(number1,number2)
    output(answer)
    

def power(num1,num2):
    if num2==0:            #any number to the power of 0 is 1
        return 1
    else:
        return num1*power(num1,num2-1)  #num2 controls how many times it executes



def output(answer):        #prints the answer
    print(f"the answer is {answer}")
    

main()