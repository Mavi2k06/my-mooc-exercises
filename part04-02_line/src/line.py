def line(times , string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)


if __name__ == "__main__":
    line(11, "x")