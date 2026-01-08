n = 6

for i in range(1, n + 1):
    # left spaces
    print(" " * (n - i), end=" ")

    if i == 1:
        print("*")
    elif i == n // 2 + 1:
        print("*" + "*" * (2 * i - 3) + "*")
    elif i == n:
        print("*" + " " * (2 * i - 3) + "*")
    else:
        print("*" + " " * (2 * i - 3) + "*")