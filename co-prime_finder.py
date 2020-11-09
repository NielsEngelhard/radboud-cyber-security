# a = lambda g: g**x
# b = lambda g, p: a(g) % p
#
# g = 3
# p = 25
#
# for x in range(0, 50):
#     print(b(g, p))

a = lambda g, x: g**x
b = lambda g, p, x: a(g, x) % p

# For the loop both g and p must be co prime.

g = 3
p = 17

stop = False
index = 1

print("at index {} number is {}".format(0, b(g, p, 0)))
while stop == False:
    if b(g, p, index) == 1:
        stop = True
    else:
        print("at index {} number is {}".format(index, b(g, p, index)))
        index = index + 1

print("the total amount of numbers in this loop is {}".format(index))


print((3**5) % 17)
