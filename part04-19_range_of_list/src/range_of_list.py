def range_of_list(my_list):
    largest = max(my_list)
    smallest = min(my_list)
    difference = largest - smallest
    return difference

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)