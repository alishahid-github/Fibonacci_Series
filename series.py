
# start
n = int(input("Enter the number where you want to see series "))
if n < -0:
    print("Enter number is not correct")
else:
    from functools import reduce
    first = [0, 1]

    for i in range(0, n - 2):
        first.append(reduce(lambda x, y: x + y, first[-2:]))

    for i in first: print(i)


# end
