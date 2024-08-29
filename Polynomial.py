# for i in range(10):
#     print((i+1)**3-i**3)

# for i in range(10):
#     print(3*i**2 + 3*i + 1) # Can't contain any even cubes

# for i in range(10):
#     print(3*(i**2 + i))

for i in range(30):
    print(((3*i+1)**3-1)/3) # This is only an integer when i = 3n+1, where n is an integer.

for i in range(30):
    print(str(12*i**3+6*i**2+i) + "   |   " + str(i*(6*i+1))) 




# i(i+1) needs to be 3 times less than 1 less than a cube

# Since i is an integer, only cubes that are of the form (3n)^3 will work, where n is an integer.

# i = a^x * b^y * c^z ... where a, b, c are prime numbers and x, y, z are positive integers
# i