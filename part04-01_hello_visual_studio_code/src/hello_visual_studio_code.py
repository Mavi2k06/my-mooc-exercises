while True:
    input_editor = input("Editor:").lower()
    if input_editor == "visual studio code":
        print("an excellent choice!")
        break
    elif input_editor == "word" or input_editor == "notepad":
        print("awful")
    else:
        print("not good")