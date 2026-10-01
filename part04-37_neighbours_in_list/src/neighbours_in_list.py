def longest_series_of_neighbours(my_list):
    current = 1
    longest = 0

    for i in range(1, len(my_list)):
        diff = abs(my_list[i] - my_list[i - 1])
        if diff == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
        
    return longest
        
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))