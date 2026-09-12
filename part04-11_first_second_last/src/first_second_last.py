def first_word(sentence):
    space = sentence.find(" ")
    return sentence[:space]

def second_word(sentence):
    first_space = sentence.find(" ")
    second_space = sentence.find(" ", first_space + 1)
    if second_space == -1:
        return sentence[first_space + 1:]
    return sentence[first_space + 1:second_space]

def last_word(sentence):
    last_space = sentence.rfind(" ")
    return sentence[last_space + 1:]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))