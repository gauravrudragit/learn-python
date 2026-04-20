def square(number):
    if 1 <= number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    toal_grains = 0
    for position in range(0, 64):
        toal_grains += 2 ** (position)
    return toal_grains
