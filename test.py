def printall(strings):
    if strings:
        head, *tail = strings
        print(head, tail)
        return printall(tail)

printall([1, 2, 3, 4, 5])
