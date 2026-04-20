def is_armstrong_number(number):
    org_no = number
    power = len(str(number))
    
    total = 0
    while number > 0:
        last_digit = number % 10
        number //= 10
        total += last_digit ** power

    return org_no == total
        
        
