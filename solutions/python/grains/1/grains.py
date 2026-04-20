def square(number):
    if number >= 1 and number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    total = 0
    for i in range(0, 64):
        total += 2 ** (i)
    return total
