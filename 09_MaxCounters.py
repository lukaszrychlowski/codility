## 100% correctness, 0% perf - > O(n*m)
def solution(N, A):
    counters = [0] * N
    for i in range(len(A)): #O(n)
        print('i = {}, A[i] = {}'.format(i, A[i]))
        if A[i] >= 1 and A[i] <= N:
            counters[A[i]-1] += 1
        else:
            for j in range(len(counters)): #O(m)
                counters[j] = max(counters) 
    return counters
    
## 100% O(n+m)
def solution2(N,A):
    counters = [0] * N
    max_no = set()
    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            counters[A[i]-1] += 1
            max_no.add(counters[A[i]-1])
            print(max_no)
        elif A[i] == N + 1 and len(max_no) > 0:
            counters = [max(max_no)] * N
            max_no.clear()
    return counters
N = 5   #no. of counters
A = [3,4,4,6,1,4,4] #represents consecutive operations
M = len(A)

print(solution2(N,A))