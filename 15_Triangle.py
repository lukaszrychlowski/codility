'''
if 0 <= P < Q < R < N
and if  A[P] + A[Q] > A[R]
        A[Q] + A[R] > A[P]
        A[R] + A[P] > A[Q]

(if array is sorted you can check only one condition and its enough: if a[i] + a[i+1] > a[i+2])

then P, Q, R is triangular 

eg for A = [10, 2, 5, 1, 8, 20]
    (0, 2, 4) is triangular
'''
def solution(A):
    A.sort()
    for i in range(0,len(A)-2):
        if A[i]+A[i+1]>A[i+2]:
            return 1
    return 0
