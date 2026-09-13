def list_sum(a, b):
    list = []
    for i in range(len(a)):
        list.append(a[i] + b[i])

    return list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))