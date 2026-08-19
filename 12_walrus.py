def very_slow_fun():
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    return 70

# a = very_slow_fun()
#if((a:=very_slow_fun())>10):
#   print(a)

# else:
#    print("Its not greater than 10")

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break
    