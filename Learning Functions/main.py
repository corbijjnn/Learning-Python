from cmath import sqrt

# The cmath module provides mathematical functions for complex numbers, including the square root function.


x = -4
y = abs(x)
print (f"The absolute value of {x} is {y}.")

# The abs() function converts negative into positive

x = 1.6239191231
y - round(x, 2)
print (f"The rounded value of {x} is {y}.")

# The round() function rounds a number to a specified number of decimal places

x = 5
y = pow(x, 3)
print (f"{x} raised to the power of 3 is {y}.")

# The pow() function raises a number to a specified power

x = 16
y = sqrt(x)
print (f"The square root of {x} is {y}.")

# The sqrt() function calculates the square root of a number

x = 10
y = max(x, 5, 20)
print (f"The maximum value among {x}, 5, and 20 is {y}.")

# The max() function returns the largest value among the provided arguments

x = 10
y = min(x, 5, 20)
print (f"The minimum value among {x}, 5, and 20 is {y}.")

# The min() function returns the smallest value among the provided arguments

x = 10
y = sum([x, 5, 20])
print (f"The sum of {x}, 5, and 20 is {y}   .")

# The sum() function calculates the total of the provided values

x = 10
y = len(str(x))
print (f"The number of digits in {x} is {y}.")

# The len() function returns the number of items in an object, in this case, the number of digits in the string representation of x

x = 10
y = str(x)
print (f"The string representation of {x} is '{y}'.")

# The str() function converts a value to its string representation

x = "10"
y = int(x)
print (f"The integer representation of '{x}' is {y}.")

# The int() function converts a string representation of a number to an integer

x = 10
y = float(x)
print (f"The float representation of {x} is {y}.")

# The float() function converts an integer to a floating-point number

x = 10
y = bool(x)
print (f"The boolean representation of {x} is {y}.")

# The bool() function converts a value to its boolean representation, where 0 is False and any non-zero value is True
