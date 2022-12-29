"""
Developed by Orlando Companioni
Date: October 2 2022

This is a simple car game that does you the user tells it
"""
isRunning=True   #boolean 

while isRunning:   #checks if the boolean is true or false
    command=input(">").upper()  #make the .upper() on the input
    if command == "HELP":
        print("start-to start the car")
        print("stop-to stop the car")
        print("quit-to exit")
    elif command =="START":
        print("car has started....Ready to go!")
    elif command=="STOP":
        print("car has stopped.")
    elif command=="QUIT":
        isRunning=False
    else:print("I dont understand that...")



