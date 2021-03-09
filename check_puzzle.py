def solve(A, B):
    sum_of_A = sum(A)
    print(sum_of_A)
    output = []
    for query in B:
        flag = True
        count = len(A)
        print("The value of the query", query)
        print("The value of count", count)
        temp = sum_of_A
        while flag:
            print("Inside while loop")
            if query > sum_of_A:
                print("Query >sum")
                output.append(count)
                flag = False
            elif query < A[0]:
                print("No phone can be bought")
                output.append(0)
                flag = False
            else:
                print("Inside else")
                for i in range(len(A) - 1, -1, -1):
                    print("Index", i)
                    print("The value of a[i]",A[i])
                    temp = temp - A[i]
                    print("The value of temp", temp)
                    count -= 1
                    print("Count",count)
                    if query >= temp:
                        print("If final got true")
                        output.append(count)
                        flag = False
                        break
    print(output)
    return output

solve([23, 36, 58, 59],[3, 207, 62, 654, 939, 680, 760])