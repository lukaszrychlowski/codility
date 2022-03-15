#100%
def solution(A):
    import heapq
    largest = heapq.nlargest(3, A) 
    smallest = heapq.nsmallest(2, A)
    
    return max(largest[0]*largest[1]*largest[2], largest[0]*smallest[0]*smallest[1])