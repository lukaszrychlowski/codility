def solution(X, A):
    steps = set([i for i in range(1, X+1)])
    frog_steps = set()
    for index, leaf in enumerate(A):
        frog_steps.add(leaf)
        if frog_steps == steps:
            return index
    return -1



'''
get frog across river, A[k] represents position of falling leaf at given time,
e.g. A[2] = 1 means that leaf falls at position 1 at timer=2sec. find earliest
possible time to cross the river

-land- X+1
------ X
------ X-1
------
------
------ 1
-frog- 0

example X=5 for
A0 = 1, A1 = 3, A2 = 1, A3 = 4, A4 = 2, A5 = 3, A6 = 5, A7 = 4
returns 6



N, X are ints in range(1, 100000)
A[k] is int in range(1, X)
'''

X = 5
A = [1,3,1,4,2,3,5,4]

def solution2(X, A):
    steps_to_be = set()
    time = 0
    for i in range(len(A)):
        if A[i] not in steps_to_be and A[i] <= X:
            steps_to_be.add(A[i])
            seconds = i
            print('steps taken: {}, time: {}'.format(steps_to_be, seconds))
    if len(steps_to_be) == X:
        return seconds
    return -1


solution2(X, A)