# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# create a dict from 2 lists
# When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.
month_dict = {key: value for (key, value) in zip(number, months)}
print(month_dict)

# set comprehension
set_a = {x for x in range(10, 20) if x not in [12, 14, 16, 18]}
print(set_a)

for x in range (10,20):
    print(x)

a = [[96], [69]]
print(map(str, a))
print(''.join(list(map(str, a))))

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)

list = [1, 2, 3, 4]

list.insert(3, 5)
print(list)

list.extend(list)
print(list)