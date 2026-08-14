def line(times , string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)

def box_of_hashes(height):
    num = 1
    while num <= height:
        line(10 , "#")
        num += 1


if __name__ == "__main__":
    box_of_hashes(5)