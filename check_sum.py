def solve(A, B):
    for i in range(0,len(A)):
        p_sum=0
        for j in range(i,len(A)):
            p_sum=p_sum+A[j]
            if p_sum==B:
                return A[i:j+1]

print(solve([1,2,3,4,5],9))