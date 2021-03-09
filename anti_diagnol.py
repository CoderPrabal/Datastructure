def solve(A):
    length_of_array = len(A)
    no_of_anti_diagnol = (2 * length_of_array) - (1)
    empty_lists = [[] for _ in range(no_of_anti_diagnol)]
    print(empty_lists)
    for i in range(0, length_of_array):
        for j in range(0, length_of_array):
            value = A[i][j]
            sum_index = i + j
            empty_lists[sum_index].append(value)
    print(empty_lists)



A = [[1, 2, 3], [3, 4, 5], [7, 8, 9]]
solve(A)
