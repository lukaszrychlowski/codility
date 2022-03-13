
def Solution(A, k):
    if len(A) > 0:
        for i in range(k):
            shifted_val = A[-1]
            print('shifting: ' + str(shifted_val))
            A.insert(0, shifted_val)
            print('A = ' + str(A))
            A.pop()
    else:
        A = A
    return A

print(Solution([], 5))