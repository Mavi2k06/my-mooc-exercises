def shortest(my_list):
    short = my_list[0]

    for word in my_list:
        if len(word) <= len(short):
            short = word

    return short

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)