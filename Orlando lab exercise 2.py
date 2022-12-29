"""
Lab 2
Set-B
Course: PROG12974
Submission date: oct 11 2022
Developed by: Orlando Companioni
Date created: oct 11 2022
Exercise 2
Gets the date of the user then outputs it 
"""

date=(input("what is the date YYYY-MM-DD: "))
#make it into a list
list=date.split("-")

#assign each value of the list to a variable
day=list[2]
month=list[1]
year=list[0]
months=["January", "February", "March", "April", "May", "June", "July",\
        "August", "September", "October", "November","December"]
newmonth=months[int(month)-1] #check the value of the month into a list

#output the converted file
print(f"Date in coverted format:{newmonth} {day},{year}")



