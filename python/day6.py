# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# create a dict from 2 lists
# When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.
month_dict = {key: value for (key, value) in zip(number, months)}
print(month_dict)