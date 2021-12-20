print("Enter a string:", end = " ")
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

def printresult(words, newstring, repetitions):
    for i in range(len(words)):
        print("Word: " + words[i])
        print("Number of repetitions: ", repetitions[i])
    print("String without duplicates: ", newstring)
    print(end = '\n')

filllists(list, words, repetitions)
newstring = " ".join(words)
printresult(words, newstring, repetitions)