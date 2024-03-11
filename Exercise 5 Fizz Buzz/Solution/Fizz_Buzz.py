def fizzBuzz(upTo):
    for num in range (1, 90):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end = '')
        elif num % 3 == 0:
            print('Fizz', end = '')
        elif num % 5 == 0:
            print('Buzz', end = '')
        else:
            print(num, end = '')



fizzBuzz(35)





