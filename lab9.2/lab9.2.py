string = input()
list = string.split()
words = []
repetitions = []

def filllists(list, words, repetitions):
    for x in list:
        if x not in words:
            words.append(x)
            repetitions.append(1)
        else:
            repetitions[words.index(x)]+=1

def printresult(words, repetitions):
    for i in range(len(words)):
        print("Word: " + words[i])
        print("Number of repetitions: ", repetitions[i])
    print("List without duplicates: ", end = " ")
    for i in words:
        print(i, end=' ')

filllists(list, words, repetitions)
printresult(words, repetitions)