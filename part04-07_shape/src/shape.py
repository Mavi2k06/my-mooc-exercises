def line(times , string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)

def shape(size, character1, height, character2):
    num = 0
    while num <= size:
        line(num, character1)
        num += 1
    bum = 1
    while bum <= height:
        line(size, character2)
        bum += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")