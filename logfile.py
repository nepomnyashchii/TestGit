def countChars(char, str):
    count = 0
    for oneChar in list(str):
        if oneChar == char:
            count = count + 1
    return count


def mylog(string):
    with open("log.txt", 'a') as f:
        f.write(str(string) +"\n")
    return

mylog("App started")
with open('sample1.txt', 'r') as f:
    lineNumber = 0
    for line in f:
        lineNumber += 1
        newString = "Line Number:" + str(lineNumber)+ "Chars Count:"+ str(countChars("s", line))
        mylog(newString)
        print(newString)
mylog("App finished")