def anagram(A):
    hashmap = {}
    for index, word in enumerate(A):
        sorted_word = "".join(sorted(word))
        if sorted_word not in hashmap:
            hashmap[sorted_word] = [index + 1]
        else:
            hashmap[sorted_word] += [index + 1]
    return list(hashmap.values())


# print(anagram(['cat', 'dog', 'god', 'tca']))
def twoSum(A, B):
    hashmap = {}
    output = []
    for i in range(0, len(A)):
        if A[i] not in hashmap.keys():
            hashmap[A[i]] = [i]
        else:
            hashmap[A[i]] += [i]
    print(hashmap)

    for i in range(0, len(A)):
        ele_to_find = B - A[i]
        print("Element to find", ele_to_find)
        if ele_to_find in hashmap.keys():
            ele_index = min([j for j in hashmap[ele_to_find] if j > i])
            print("The element index is ", ele_index)
            output.append(min(ele_index, i))
            output.append(max(ele_index, i))
            print(output)

    return []


print(twoSum([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8],
             -3))
