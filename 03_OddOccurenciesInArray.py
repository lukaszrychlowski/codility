def solution(A):
    from collections import Counter
    unique_element = Counter(A).most_common()[-1][0]
    return unique_element
A = [9, 3, 9, 3, 9, 7, 9, 1, 1]
unique_element = solution(A)
print(unique_element)