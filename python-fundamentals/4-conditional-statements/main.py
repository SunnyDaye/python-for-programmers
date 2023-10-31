# The "if" statement
num = 5

if num == 5:
    print("5 is the number")

if num > 5:
    print("Woah thats a big number")

# Conditions with logical operators
num = 12
if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    print("This number is a multiple of 2, 3, and 4!")

if num % 5 == 0 or num % 6 == 0:
    print("This number is a multiple of 5 and/or 6")

# Nested conditional
num = 63
if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is within the 60 - 70 range.")

# Creating and editing values in if statements
num = 10
if num > 5:
    num = 20
    new_num = num * 5

print(num)
print(new_num) # Notice how creating a variable with the scope of the if statement adds the variable to the scope of the whole file


# The "if-else" statement
num = 60
if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")

# Conditional expressions - uses an if-else statement to return an output depending on the condition
num = 65
output = "This number is less than or equal to 50" if num <= 50 else "This number is greater than 50"
print(output)


