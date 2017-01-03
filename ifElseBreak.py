"""
    this is multiline comment
"""

i = 1
for i in range(1, 50):
    if i % 2 == 1:
        print(i, " is a Prime Number...")
    else:
        print("...")

print("\n")

x = 0
for x in range(20):
    if x < 15:
        print(x)
    else:
        print("\n15 encountered, exiting...")
        break
