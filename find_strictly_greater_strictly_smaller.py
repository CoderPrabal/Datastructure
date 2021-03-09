def solve(A):
    A.sort()
    # print(A)
    flag_even = True
    flag_odd = True
    max_min_list = []
    while (flag_even):
        for elem in range(len(A) - 1, -1, -1):
            if A[elem] % 2 == 0:
                max_min_list.append(A[elem])
                flag_even = False
    while (flag_odd):
        for elem in range(0, len(A)):
            if A[elem] % 2 != 0:
                max_min_list.append(A[elem])
                br
                flag_odd = False
    print(max_min_list)
    return max_min_list[0] - max_min_list[1]

solve([-98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ])