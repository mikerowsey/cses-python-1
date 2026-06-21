# get input from user and convert to integer
n = int(input())

# create a list and add n to it
a = [n]

while True:
    if n == 1:
        break

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    a.append(n)

print(" ".join(map(str, a)))

