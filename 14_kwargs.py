def marks(**kwargs):
    # kwargs is a dictionary with all the key-value pairs passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(John=90, Jack=43, Zaid=100, Ali=75, Marie=67)