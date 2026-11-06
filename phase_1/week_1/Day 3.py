# Start at 0 and use += to reach 10 in two steps

x = 0
x += 17
x -= 7
print(x) 

# Use -= to subtract from a score 

score = 100
score -= 60
print(score)

# Double a value with *= 

x = 1
x *= 67
print(x)

# Build a string 'Python' using += from 'Py' 

x = "py"
x += "thon"
print(x)

#  Create variables for your name, age, height, and

x = "badri"
age = 20
height = 5.9
is_student = True
print(type(x), type(age), type(height), type(is_student))

# Assign 1, 2, 3 to x, y, z in one line

x , y , z = 1, 2, 35
print(x, y, z)

# Assign the value 0 to three variables in one line

a = b = c = 8
print(a, b, c)

# Swap two variables without a temp variable 

_x = 6
_y = 7
_x, _y = _y, _x
print(_x, _y)   

# Unpack a 2-element list into two variables 

a, b = [1, 2]

# Unpack a 3-item list of fruits into three names

fruits = ["chestnut", "banana", "mango"]

# Assign name and age together from two values 

name, age = "baderi", 25

# Print 'Age: 25' by concatenating with str()

print("Age: " + str(age))

# Swap three variables without a temp variable 

a =1 
b = 2
c = 3
a, b, c = c, a, b
print ("a =",a,"b =", b,"c =" ,c)

# Assign multiple values then swap two of them

x = 4
y = 5
z = 6
x  = x *z
y  = y *z
x,y =y,x
print(x, y,)