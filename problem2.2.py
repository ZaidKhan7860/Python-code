num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))

operation = input("Choose operation: ")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 + num2)
    case "/":
        print(num1 / num2)