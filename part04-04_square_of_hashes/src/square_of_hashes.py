def line(times,string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)

def square_of_hashes(size):
    num = 1
    while num <= size:
        line(size, "#")
        num += 1

if __name__ == "__main__":
    square_of_hashes(5)
