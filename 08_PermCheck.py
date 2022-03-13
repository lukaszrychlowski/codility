### sum comparision, 77%
def solution(A):
    n = len(A)
    check_sum = (n * (n+1)) // 2 
    sum_A = sum(A)
    print('check_sum = {}, sumA = {}'.format(check_sum, sum_A))
    if sum_A == check_sum:
        return 1
    else:
        return 0

## compare sets, 100%
def solution2(A):
    check = set()
    for i in range(1,len(A)+1):
        check.add(i)
    if set(A) == check:
        return 1
    else:
        return 0

A = [4, 1, 3, 2]
print(solution2(A))