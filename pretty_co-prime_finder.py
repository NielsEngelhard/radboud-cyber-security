from math import gcd as bltin_gcd

# lambdas with "calculation logic"
gToThePowerOfX = lambda g, x: g ** x
gToThePowerOfXModuloP = lambda g, p, x: gToThePowerOfX(g, x) % p


def print_loop(generator, modulus):
    if not numbers_are_co_prime(generator, modulus):
        return

    stop = False
    index = 1

    # print the first line for the value 0 (which is always zero, N^0 is always 0)
    print("at index {} number is {}".format(0, gToThePowerOfXModuloP(generator, modulus, 0)))

    while not stop:
        current_number = gToThePowerOfXModuloP(generator, modulus, index)

        if current_number == 1:  # when there is a 1 in the loop (except N^1), the loop is done
            stop = True
        else:
            print("at index {} number is {}".format(index, current_number))
            index = index + 1

    print("the length of this loop is {}".format(index))


def numbers_are_co_prime(number1, number2):
    result = bltin_gcd(number1, number2)
    if result == 1:
        print("{} and {} are co-prime".format(number1, number2))
        return True
    else:
        print("{} and {} are not co-prime and can both be divided by {}".format(number1, number2, result))
        return False

# example of use

# --- definition of co prime ---
# When two numbers have no common factors other than 1.
#
# In other words there is no whole number that you could divide them both by exactly (without any remainder).
#
# For example 8 and 4 are not co prime because they both can be divided by 2 (and get a whole number)
# For example 7 and 17 are co prime because they both can only be divided by 1 (and get a whole number)
# ------------------------------


G = 3  # generator
P = 17  # modulus

print_loop(G, P)  # will work, because 3 and 17 are co prime

G = 2  # generator
P = 8  # modulus

print_loop(G, P)  # will not work, because 2 and 8 are not co prime
