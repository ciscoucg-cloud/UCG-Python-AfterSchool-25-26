# Guess the Number Game

#The correct Numbur 

secritnum = 4


guess =0 


# create a while loop

while secritnum != guess :
    if guess > secritnum:
        print("No your number is too high guess again")
        guess =int(input("Enter a number between 1 and 15: "))
    if guess < secritnum:
        print("No your number is too lwo guess again")
        guess =int(input("Enter a number between 1 and 15: ")) 
else:
    print("🎉You got it right")