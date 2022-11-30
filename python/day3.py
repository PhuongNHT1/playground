a = 10
b = 20

def sum(a, b):
    print("Sum of", a + b)

sum(7, 10)

# this is a list
print()
print("This is list example")

list = [1, 2, 3, 4, 5, "hello"]
list.insert(len(list), 15)
list.extend([16, 17, 18])
list.pop(4) # pop number 5, at 4th position
print(*list, sep=', ')

# this is a tuple
print()
print("This is tuple example")

my_tuple = (4.5, "hello", 1, True, "hello")
print(my_tuple[0])
print("Index of 4.5", my_tuple.index(4.5))
print(my_tuple.count(1))

# Tuple is immutable
# my_tuple[0] = 8

# This is a set
print()
print("This is set example")
# a set do not allow duplication
a_set = {1, 2, 3, 4, 5, 5}
a_set.add(6)
a_set.remove(5) # remove all 5s
a_set.discard(1) # same as .remove
print("Set a: ", a_set)

b_set = {6, 7, 8, 9}
print("Set b: ", b_set)
print("- Union: ", a_set.union(b_set))
print("- Or: ", a_set | b_set)
print("- Intersec: ", a_set.intersection(b_set))
print("- Difference: ", a_set.symmetric_difference(b_set))


# using arg
def sum_of(*arg):
    sum = 0
    for x in arg:
        sum += x
    return sum

print(sum_of(4, 5, 6))
print(sum_of(4, 5, 6, 5))

