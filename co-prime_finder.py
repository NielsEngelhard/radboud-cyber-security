gToThePowerOfX = lambda g, x: g ** x
gToThePowerOfXModuloP = lambda g, p, x: gToThePowerOfX(g, x) % p

# For the loop both g and p must be co prime.

G = 3  # generator
P = 17  # modulus

stop = False
index = 1

# print the first line for the value 0 (which is always zero, N^0 is always 0)
print("at index {} number is {}".format(0, gToThePowerOfXModuloP(G, P, 0)))

while not stop:
    currentNumber = gToThePowerOfXModuloP(G, P, index)

    if currentNumber == 1:  # when there is a 1 in the loop (except N^1), the loop is done
        stop = True
    else:
        print("at index {} number is {}".format(index, currentNumber))
        index = index + 1

print("the length of this loop is {}".format(index))
