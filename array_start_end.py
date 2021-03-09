def solve(A, B):
    start_pointer = B
    #print("Start pointer",start_pointer)
    end_pointer = len(A)-1
    #print("End pointer ",end_pointer)
    max_sum=0
    current_sum=sum(A[0:start_pointer])
    #print("The current sum is ",current_sum)
    while start_pointer!=-1:
        max_sum=max(max_sum,current_sum)
        #print("The max sum is ",max_sum)
        current_sum=current_sum-A[start_pointer-1]+A[end_pointer]
        #print("The current_sum is ",current_sum)
        start_pointer=start_pointer-1
        end_pointer=end_pointer-1
    return max_sum



A=[5,-2,3,1,2]
B=3
print(solve(A,B))