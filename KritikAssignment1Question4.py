def bunny(x):
    if x >= 0 and x <= 1:
        n = 0
        running = 0

        def error(a, b):

            return abs((a ** ((2 * b) + 1)) / ((2 * b) + 1))

        while error(x, n) > 0.0001:
            n += 1

        for i in range(n):
            current = ((-1) ** i) * (x ** ((2 * i) + 1)) / ((2 * i) + 1)
            running += current

        return (running, n, error(x, n))
    else:
        print("Error: Input must be between 0 and 1")
        return None

x = float(input("Enter your number: "))
print(bunny(x))
