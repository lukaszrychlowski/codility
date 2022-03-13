def solution(A):
    B = list(range(1,len(A)+2))
    return sum_of(B)-sum(A)

def sum_of(A):
    len_A = len(A)
    sum = 0.5 * len_A * (len_A + 1)
    return int(sum)

A = [1,2,3,5]