def ordinalSuffix(number):
    # Convert number to string
    num_str = str(number)
    
    # Determine the appropriate suffix
    if 10 <= number % 100 <= 20:
        suffix = 'th'  # Handle exceptions for 11, 12, 13
    else:
        last_digit = number % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    
    return num_str + suffix

# Test cases
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(21) == '21st'
assert ordinalSuffix(22) == '22nd'
assert ordinalSuffix(23) == '23rd'
assert ordinalSuffix(101) == '101st'
assert ordinalSuffix(112) == '112th'
assert ordinalSuffix(213) == '213th'

print("All tests passed!")
