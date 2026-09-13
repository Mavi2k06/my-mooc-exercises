def length(my_list):
    count = 0
    while count < len(my_list):
        count += 1
    return count

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)