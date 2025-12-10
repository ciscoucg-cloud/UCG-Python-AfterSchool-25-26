#Program Description: The purpose of this progrom is to reverse the number entered by the user


# Take the number from the user as a sting
n = input("Enter a number: ")

rev = ""              # This will stre the 
i = len(n) - 1

while i >=0:
    rev = rev + n[i]
    i -= 1

print(f"The number reversed is : {rev}")
