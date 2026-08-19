s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

a = len(s)
# print(a)
# print(s.upper(), s)
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# text = " \nhello world "
# print(text.strip()) # output: "hello world"
# print(text.lstrip()) # output: "hello world "
# print(text.rstrip()) # output: " hello world"


#text = "Python is fun and fun and fun"
#print(text.find("s")) # output: 7 Index of first occurence
#print(text.replace("fun", "awesome"))


#text = "Apples,Bananas,Pineapples"
#print(text.split(","))
#print(",".join(['Apples', 'Bananas', 'Pineapples']))

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False