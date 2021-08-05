"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.
    NOTE: chars variable can contain any even number of characters.
        the len() function can be used to figure out the length of a string
    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>
"""

chars = "<<[]]]"  # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]
length = len(chars)
index = int(length/2)


# Your code below:
result = chars[:index] + word + chars[index:]
print(result)