"""
Developed by Orlando Companioni
Date:sept 27 2022

 User enters input and we calculate it and output it
 """
num=""
newnum=0
while num!=0:    #run as long as not = 0
    num=int(input("Enter an integer or enter 0 to end "))
    newnum+=num

#output the total value
print(f"your total is {newnum}")
