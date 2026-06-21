# get input from user and convert to integer
n = int(input())

# create a list and add n to it
a = [n]

# loop until done
while True:
    # if n == 1, we're done.
    if n == 1:
        break

    # check if n is even
    if n % 2 == 0:
        # even so divide by 2
        n = n // 2
    else: # it's odd
        # multiply by 3 and add 1
        n = 3 * n + 1
    # add current n to to list
    a.append(n)

# write list as a string, separate values with a space
print(" ".join(map(str, a)))

