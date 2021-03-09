def addBinary(A, B):
    # find the max length between a and b
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    print(A)
    print(B)
    # intialize the result
    result = ''
    # intialize the carry
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if A[i] == '1' else 0
        r += 1 if B[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0: result = '1' + result
    return result.zfill(max_len)


print(addBinary("1010110111001101101000", "1000011011000000111100110"))
