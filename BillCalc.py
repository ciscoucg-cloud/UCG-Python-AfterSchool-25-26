# Program Description: Calculates bill

#Asking user for BILL amt

bill = int(input("Enter Bill amt: "))

# Asking user for no. of people

people =int(input("Enter no. of people sharing the bill: "))

# Defin tax and tip rates

tax_rate = 0.0825
tip_rate = 0.15

#formula to caluculate  tax, tip and total 
tax = bill * tax_rate 

tip = bill * tax_rate

total = bill * tax + tip

#Calculate amt each person owes
per_person = total /people

#Printing everything

print("Restaurant Bill Calculater")
print("---------------------------------")
print(f"Orginal Bill: {bill}")
print(f"sales Tax: {tax}")
print(f"Tip 15%  {tip}")
print(f"Here is the total bill {total}")
print(f"Each person's share  {per_person}")
