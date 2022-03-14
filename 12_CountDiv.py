'''
giveen three ints A, B, K, return no. of ints in range(A, B) that are divisible by K
e.g. for A = 6, B = 11, K = 2 returns 3 (6,8,10)

efficient!
A,B in range(0,2*10^9)
K in range(1, 2*10^9)
)

Rachel says:
March 24, 2015 at 1:26 pm
Clearly the size of the interval [A,B] determines the answer, however we distinguish the two different cases because whether or not K divides A affects the answer. Take K=10 for example. If A=20 and B=30 then the answer is 2. If A=21 and B=31 then the answer is 1 despite the fact that the difference A-B here is the same. Since K divides A in the first instance the answer is one greater.
Now, let a = A%K (i.e. A = a (mod K))
so we may write A = a + mK for some integer m
here mK is the largest multiple of K that is less than or equal to A
and A – A%K = a + mK – a = mK
(note if A is a multiple of K then a=0)
the number of multiples of K in [A,B] is the same as the number of multiples of K in [mK,B] if a=0 (i.e. K divides M) and one less than this if a>0 (i.e. K doesn’t divide M), because in this case mK is not in the interval [A,B]
Now, the number of multiples of K in [mK,B] is equal to the number of multiples of K in the interval [0,B-mK], which is floor((B-mK)/K) +1 (the plus one is there because 0 is a multiple)
so the answer is
(B-(A-A%K))//K if A%K>0
and
(B-(A-A%K))//K + 1 = (B-A)//K + 1 if A%K==0
I hope my explanation makes sense!
'''

def solution(A, B, K):
    divisible = []
    numbers = list(range(A, B+1))
    for number in numbers:
        if number % K == 0:
            divisible.append(number)
    return len(divisible)

def solution2(A, B, K):
    if A % K == 0:  return (B - A) // K + 1
    else:           return (B - (A - A % K )) // K


