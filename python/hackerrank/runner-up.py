if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # remove duplicated value by casting to set
    my_set = set(arr)

    # get max
    max_scrore = max(my_set)

    # remove the max score
    my_set.remove(max_scrore)
    print(max(my_set))