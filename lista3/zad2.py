def change_newline(file_path):
    file = open(file_path, "rb")
    text = file.readlines()
    file.close()

    file2 = open(file_path, "wb")

    for line in text:
        if b"\r\n" in line:
            line = line.replace(b"\r\n", b"\n")
        else:
            line = line.replace(b"\n", b"\r\n")
        file2.write(line)

    file2.close()
change_newline(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\test\er.txt")
