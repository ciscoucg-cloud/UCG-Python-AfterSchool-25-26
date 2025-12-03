# Countdown Timer Program
#Program Desciption: This program counts down from a user-given number to 1

#importing time module to add 1 secon delay
import time
# Ask the user to enter a number to start counting down from 
number = int(input("Enter a number to start the contdown: "))

#keep loopinmg as long as the number is greater then 0
while number > 0: 
    print(number) #Print the cerrent number
    time.sleep(1) #Wait for 1 second before continuig
    number -= 1   # Subtract 1 from number each time

# Once the loop end, print a message
print("🎉 Time is up!")

