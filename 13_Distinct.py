'''
75%
▶extreme_negative 
sequence of negative elements, length=5 ✘WRONG ANSWER 
got 2 expected 3
▶ medium2 
chaotic sequence of value sfrom [0..1K], length=200 ✘WRONG ANSWER 
got 178 expected 179
▶ medium3 
chaotic sequence of values from [0..10], length=200 ✘WRONG ANSWER 
got 10 expected 11
'''
def solution(A):
    A.sort()
    count = 0
    if len(A) == 1:
        return 1

    if len(A) != 0 and A == [A[0]]*len(A): 
        return 1

    for i in range(len(A)):
        try:
            if A[i] != A[i+1]:
                count += 1
        except IndexError:
            if A[-1] == A[-2]:
                pass
            else:
                count += 1

    return count