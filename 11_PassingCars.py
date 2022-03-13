'''
A = [0, 1, 0, 1, 1]

n   zeroes  cars
0   1       0
1   1       1
2   2       1
3   2       3
4   2       5
'''

def solution(A):
    zeroes = 0
    passing_cars = 0
    for i in A:
        if passing_cars > 1000000000:
            return -1
        elif i == 0:
            zeroes += 1
        else:
            passing_cars += zeroes
    return passing_cars

A = [0, 1, 0, 1, 1]
print(solution(A))