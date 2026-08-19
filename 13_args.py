def sum(*args):
    # args will be a tuple of all the values passed to sum
    total = 0
    for n in args:
        total += n
    return total


print(sum(422, 4, 5, 9))