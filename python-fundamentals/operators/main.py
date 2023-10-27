# Arithmetic Operators
print(10 + 5) # adds --> 15
print(10 - 5) #  subtracts --> 5
print(10 * 5) # multiplies --> 50
print(10 / 5) # divides --> 2
print(10.2 // 5) # divies then rounds down --> 2
print(11 % 5) # returns remainder after division --> 1
print((10 - 5) * 2) # changes order of precendence --> 10

# Comparison operators
print(2 > 5) # --> false
print(5 >= 5) # --> true
print(2 < 5) # --> true
print(6 <= 5) # --> false
print(7 == 9) # --> false
print(7 != 9) # --> true
print({"someKey": "someValue"} is {"someKey": "someValue"}) # compares objects for equality --> false because two different memory address
print({"someKey": "someValue"} is not {"someKey": "someValue"})# compares objects to inequality --> true
x = ["apple", "banana", "cherry"]
y = x
print(y is x) # --> true because y points to the value at the memory address of x

print(1 is 1) # --> true because operands are primitive data types
print("hello" is "hello")

# Assigment operators
x = 8
y = set(["a","b","c"])
z = set(["d","e","f"])
x += 10 # adds to value of x then assiggns new vaule to x --> 18
x -= 9
x *= 5
x **= 2
x /= 9
x //= 2
x %= 2
print(x)
y |= z # union or OR operator of two collections --> {a ,b, c, d, e, f}
y &= z # returns commonalities between sets ---> {d, e, f}
y ^= z # prints the differences between sets ---> {}
y = 5
y >>= 3  #bit shift right then assign --> 0
y <<= 3 # bit shift left then assign --> 0
print(y)

#Logical Operators
print(True and False) #--> false because both operands must be true
print(True or False) #--> true because atleast one operands is true
print(not True) # --> inverse of True ~ False

#Bitwise Operators
set1 = set(("a1","b1","c1"))
set2 = set(("a2","b2","c2"))
READ_PERMISSION = 4
WRITE_PERMISION = 2
ADMIN_PERMISSION = 1
user_permissions = READ_PERMISSION | WRITE_PERMISION | ADMIN_PERMISSION
print(user_permissions) # the bitwise or operator adds the bits of each operand together one bit at a time. Logically, we are assigning all permissions to the user. The user has read or write or admin permissions
print((user_permissions & WRITE_PERMISION) == WRITE_PERMISION) # the bitwise and operator multiplies the bits of each operand one at a time. Here were seeing if a user has a specific permission. If the bitwise and operation returns the permission, then the user has that permission
print(user_permissions ^ WRITE_PERMISION) # the bitwise xor operator performs an xor operation on each bit of the operands. This takes away the write permission and returns the other two permissions



