Write a convert_to_fahrenheit() function with a degrees_celsius parameter.

This function returns the number of this temperature in degrees Fahrenheit.

Then write a function named convert_to_celsius() with a degrees_fahrenheit parameter and returns a number of this temperature in degrees Celsius


Use these two forumlas for converting between Celsisus and Fahrenheit 

Fahrenheit = Celsius x (9/5) + 32

Celsius = (Fahrenheit - 32) x (5/9)

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert convertToCelsius(0) == -17.77777777777778

assert convertToCelsius(180) == 82.22222222222223

assert convertToFahrenheit(0) == 32

assert convertToFahrenheit(100) == 212

assert convertToCelsius(convertToFahrenheit(15)) == 15
