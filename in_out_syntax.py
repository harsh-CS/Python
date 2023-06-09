if __name__ == '__main__':
    x = open('C:\\Users\\harsh_ph1dmia\\Desktop\\file.txt')
    print(x.read())
    x.seek(0)  # when we read the file curser goes to the end of the file so we need to reset the cursor
    print(x.readline())  # read a single line
    x.seek(0)
    print(x.readlines())  # read all the line in line format
    x.close()
    with open('C:\\Users\\harsh_ph1dmia\\Desktop\\file.txt')as f:
        contents = f.read()
    print(contents)
    with open('C:\\Users\\harsh_ph1dmia\\Desktop\\file.txt', mode='r')as f:
        contents = f.read()
    print(contents)
    with open('C:\\Users\\harsh_ph1dmia\\Desktop\\file.txt', mode='a')as f:
        contents = f.write('/nThis is append')
