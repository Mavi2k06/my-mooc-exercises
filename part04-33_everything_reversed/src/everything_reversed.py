def everything_reversed(my_list):
    new_list = []
    i = len(my_list) - 1

    while i >= 0:
        string = ""
        j = len(my_list[i]) - 1

        while j >= 0:
            string += my_list[i][j]
            j -= 1

        new_list.append(string)
        i -= 1

    return new_list


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)