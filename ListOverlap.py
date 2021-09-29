# LIST OVERLAP


a = [1, 2, 3, 5, 8, 13, 15, 21, 27, 28, 29, 30, 34, 44, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 27, 43, 44, 45]
c = []
d = []

for elem in a:
    if (elem in a) and (elem in b):
        c.append(elem)
        continue
    elif (elem in a):
        d.append(elem)
    else:
        break

print("\nThe numbers that are included in both lists are:\n{}".format(c))








# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
