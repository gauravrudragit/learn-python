def square(number):
    """ Calculates the number of grains on this postion    
    """
    if 1 <= number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    """ Calculates the total number of grains on the board
    """
    toal_grains = 0
    for position in range(0, 64):
        toal_grains += 2 ** (position)
    return toal_grains
