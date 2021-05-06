print("Hello, World", end="!\n")
# print has 2 keyword arguments 
#   sep - separator between each argument
#       default = " "
#   end - what goes at the end of the printed statement
#       default = "\n"
print("Print can handle octals", 0o123)
print("and hexadecimals!", 0x123)
#when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
# // is an integer divisional operator (floor division)
print(9 % 6 % 2)
#variables 2.4.1.7 LAB
john=3
mary=4
adam=5
print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
print(total_apples)
#2.4.1.9 LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers * (1 / 1.61)

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#2.4.1.10 LAB
x =  0
x = float(x)
y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
print("y =", y)
