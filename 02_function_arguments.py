# Positional Arguments
def add(a, b):  
    x = a + b
    return x


c = add(3, 5)
print(c)

# Default Arguments
def add(a, b, plus=0):
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)


# Keyword Arguments
def students(name, age):
    print(f"Name: {name}, Age: {age}")

students(age=21,name="zaid")