def square(number):
    if 1 <= number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    sum = 0
    for square in range(0, 64):
        sum += 2 ** (square)
    return sum
