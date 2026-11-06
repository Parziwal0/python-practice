# Print your name, age, and city on three separate lines

print("name","age","city",sep="-")

# Print three values separated by hyphens using sep

print("1","2","4",sep="-")

# Print 'Loading...' then 'done' on the same line using end

print("loding...",end="")
print("done")

# Print a date as 2026/27/28 using sep

print("2026","27","28",sep="/" )

# Print a date as 2024/01/15 using sep

print("nizampet\nminnahar")

# Use \t to print a name and score in aligned columns 

print("badri\t67 \\ 100")

# Print a Windows file path with literal backslashes

print("C:\\Users\\Badri\\Documents\\Python")

# Print a sentence containing double quotes 

print('i said to him \"hello\"')  # OR print("i said to him "hello"")

# Build a sentence from name and age using an f-string

name="Badri"
age=13
print(f"{name} is {age} years old.")

# Build the same sentence using comma-separated print

print("My","name","is",name,sep=",") 

#  Build the same sentence using + and str()

print("My","age","is",str(age),sep=",")

# Print pi rounded to 2 decimal places with an f-string

pi=3.14
print(f"{pi:.2f}")

# Print 1250000 with thousands separators

price =1250000
print(f"{price:,}")

# Print 0.256 as a percentage with one decimal

x=0.256
print(f"{x:.1%}")

# Print a 3x3 box of stars using \n in one string

print("***\n***\n***")  
""" Or use print("***" * 3) to print *** three times in a row. """












