def isOdd(num):
    return num % 2 != 0

def isEven(num):
    return num % 2 == 0

# Test assertions
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True

assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False

print("All tests passed!")

