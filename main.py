import time
import sys


name = "Test."
print(chr(27) + "[2J")
username = input("What is your name: ")
menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"
print("What would you like to order",username,"?","Take a look at our menu:", menu)
order = input()
price = 60
quantity = input("How many would you like:\n")
total = price * int(quantity)
print("You ordered:", quantity, order)
print("your total is:",total)
time.sleep(8)
print(chr(27) + "[2J")
print("Preparing your", order)
time.sleep(10)
print(chr(27) + "[2J")
thankyou = "Thank you for shopping at Simple_Barista."
time.sleep(8)
for char in thankyou:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print(chr(27) + "[2J")
