#Varible to store user name
name =input("Enter your name: ")

#While loop will run as long as the varible name has nothing stored in it
while name =="" or not name.isalpha():
    print("Name entered is invalid")
    #Asking the user to enter name in case they didn't type 
    name =input("Enter your name: ")

#Exit out of loop once finished
print(f"Hello {name}")
