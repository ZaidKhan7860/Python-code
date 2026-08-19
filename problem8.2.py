def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_details(name="John", age=21, city="Bihar")
# Output:
# name: John
# age: 21
# city: Bihar