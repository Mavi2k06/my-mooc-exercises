def sum_of_positives(my_list):
    num = 0
    for p in my_list:
        if p > 0:
            num += p

    return num

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)