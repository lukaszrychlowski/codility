N = 1041223
N = bin(N)[2:]
print(N)
print(N[len(N)-1])
counter = 0
counters = []

for i in range(len(N)):
        if int(N[i]) == 0:
            counter += 1
        elif int(N[i]) == 1:
            counters.append(counter)
            counter = 0
        elif int(N[len(N)-1]) == 0:
            counter = 0
print(max(counters))