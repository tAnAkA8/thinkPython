def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print('no')
    else:
        print('yes')

is_triangle(1, 1, 10)
#no