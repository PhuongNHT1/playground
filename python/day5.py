str = "racecar"

def reverse_str(sample):
    return sample[::-1]
    # str[start:stop:step]

if reverse_str(str) == str:
    print("palindrom")

print(reverse_str("1234"))