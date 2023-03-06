if __name__ == '__main__':
    student_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_dict[name] = score

    sorted_dict = dict(sorted(student_dict.items(), key=lambda x: (x[1], x[0])))
    # print(sorted_dict)

    # get lowest score
    lowest = 9999;
    name = list(sorted_dict.keys())
    value = list(sorted_dict.values())
    print(name)
    print(value)
    i = 0
    while (value[i] == value[i + 1]) and (i<len(name)):
        i = i + 1
    else:
        i = i + 1
        while (value[i] == value[i + 1]) and (i<len(name)):
            print(name[i])
            i = i + 1
