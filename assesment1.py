lst = [x*y for x in range(5) if x % 2 == 0 for y in range(3)]

print(lst)

print("X"*20)

for x in range(5):
    if x % 2 == 0:
        for y in range(3):
            print(x*y)
