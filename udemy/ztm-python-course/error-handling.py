# Exercises
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a value')
        continue
    except ZeroDivisionError:
        print('please dont enter zero. get the toddler off the keyboard')
        break
    else:
        print('no error')
        break
    finally:
        print('runs at the end regardless')
