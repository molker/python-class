# Exercise First Gui
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
pixel = '*'
space = ' '

def print_pixel(value):
    if value:
        print(pixel, end='')
    else:
        print(space, end='')

for row in picture:
    for col in row:
        print_pixel(col)
    print()