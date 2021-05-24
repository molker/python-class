# print("Hello, World", end="!\n")
# print has 2 keyword arguments 
#   sep - separator between each argument
#       default = " "
#   end - what goes at the end of the printed statement
#       default = "\n"
# print("Print can handle octals", 0o123)
# print("and hexadecimals!", 0x123)
#when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
# // is an integer divisional operator (floor division)
# print(9 % 6 % 2)
#variables 2.4.1.7 LAB
john=3
mary=4
adam=5
# print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
# print(total_apples)
#2.4.1.9 LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers * (1 / 1.61)

# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#2.4.1.10 LAB
x =  0
x = float(x)
y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
# print("y =", y)
#2.6.1.11 LAB
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# Write your code here.
dura_hours = dura // 60 
dura_mins = dura % 60

# print(dura_hours)
# print(dura_mins)

hour += dura_hours
mins += dura_mins

# if hour > 24:
#     hour -= 24
# if mins > 60:
#     mins -= 60
#     hour += 1

# print(hour, mins, sep=":")
#3.1.1.4 LAB
# n = int(input("enter n: "))
# print( n >= 100)
#3.1.1.10 LAB
# plant = input("Enter Spathiphyllum please I'm begging you: ")
correct = "Spathiphyllum"
# if plant == correct:
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif plant.lower() == correct.lower():
#     print("No, I want a big Spathiphyllum!")
# else: 
#     print("Spathiphyllum! Not ", plant, "!")

