a = input()
w1 = a.split()
w2 = {}
for i in w1:
    if i in w2:
        w2[i] += 1
    else:
        w2[i] = 1
for i in w2:
    print("Number: " + i)
    print("Number of repetitions: ", w2[i])