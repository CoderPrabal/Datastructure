def solve(A):
    output = 0
    for i in range(0, len(A)):
        if i == 0:
            output += (0.5 * A[i])
            print("First",output)
        else:
            output += abs((0.5) * (A[i] - A[i - 1]))
            print(output)
            output +=1
            print(output)
            print("Middle", output)
    output += abs(0.5 * A[len(A)-1])
    print("Final", output)

    return int(output)

A=[2,1,3]
solve(A)