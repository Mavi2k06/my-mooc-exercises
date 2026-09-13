def distinct_numbers(my_list):
    dist = []

    for i in (my_list):
        if i not in dist:
            dist.append(i)
    dist.sort()
    return dist

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))