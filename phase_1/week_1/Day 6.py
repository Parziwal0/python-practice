# Print your name, course, and year on three lines using one print with \n

print("badri\nPython\n2026")

#  Print '1 | 2 | 3' using sep 

print(1, 2, 3, sep=" | ")

#Build 'Asha is 25' three ways: f-string, comma, and + 

print("Asha", "is", "25")
print("Asha" + "is" + "25")
print(f"Asha is 25")

# Swap two variables and print before/after 

x =2
y=4
print("before swap = ",x ,y)
x, y = y, x
print("after swap = ",x ,y,)

#  Assign 0 to three counters in one line

a = b = c = 0
print( a , b , c )

# Convert '2026' to int, add 1, print as a string message

year = int('2026')
year += 1
print(f"The next year is {year}")

# Print pi to 3 decimal places

pi = 3.1415
print(f"Pi is {pi:.3f}")    

# Read a number with input(), double it, and print

num = int(input("Enter a number: "))*2
print("Double of your number is", num )

# Print a receipt line: item, qty, price with aligned tabs 

item = "Apple"
qty = 5
price = 1.29
print("Item \t Qty \t Price")

# Write a mini profile: name, age, city, student(bool) via f-string 
name = "Badri"
age = 13
city = "goa"
student = True
print(f"Name: {name} \n Age: {age} \n City: {city} \n Student: {student} ")