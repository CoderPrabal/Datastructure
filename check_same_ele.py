def solve(A, B):
    hash_a = {}
    hash_b = {}
    lenA = len(A)
    lenB = len(B)
    output = []
    for i in range(0, lenA):
        if A[i] not in hash_a:
            hash_a[A[i]] = 1
        else:
            hash_a[A[i]] += 1
    for i in range(0, lenB):
        if B[i] not in hash_b:
            hash_b[B[i]] = 1
        else:
            hash_b[B[i]] += 1
    print(hash_a)
    print(hash_b)

    for key, value_a in hash_a.items():
        if key in hash_b:
            value_b = hash_b[key]
            times = min(value_a, value_b)
            output += [key] * times

    print(output)


A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]
solve(A, B)
