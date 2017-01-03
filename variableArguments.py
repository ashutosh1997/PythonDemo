def add(*args):
    total = 0
    for x in args:
        total += x
    print(total)

add()
add(5, 2)
add(5, 6, 8, 10, 14, 1)
add(5, -4)
