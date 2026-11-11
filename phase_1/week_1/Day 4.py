#Create an int, a float, and a complex number; print each type

x = 13
y = 67.9
z = 3 + 5j
print(type(x), type(y), type(z))

# Show that Python ints have no overflow (2**100)

print(2**100)

# Use underscores as digit separators in a large int

x = 100_00_0
print(x)

# Get the real and imaginary parts of 2+3j 

z = 2 + 3j
print(z.real) 
print(z.imag) 
print(type(z)) 

# Write a string with an apostrophe two different ways 

massage = "I'm learning Python"
massage = 'I\'m learning Python'

# Write a 3-line string using triple quotes

massage = """I'm learning Python.
i love it """

# Slice the first three characters of 'Python' 

y = "Python"
print(y[0:3])

# Get the length of a string

print(len(y))

# Concatenate and repeat strings 

print(y + " is fun!")

# Uppercase, lowercase, and strip a string

print(y.upper())
print(y.lower())

#  Split 'a,b,c' on commas

print("a,b,c" . split(","))

# Create a None variable and test it with is None 

z = None
print(type(z))

# Count Trues in a list using sum()

_list = [True, False, True, True]
print(sum(_list))

#Get the length of a string 

print(len(y))

# Slice the first three characters of 'Python' 

print(y[0:3])