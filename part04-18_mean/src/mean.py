def mean(my_list):
    numbers = len(my_list)
    sum1 = sum(my_list)
    me_an = sum1 / numbers
    return me_an

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)