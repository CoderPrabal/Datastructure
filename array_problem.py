def solve(A):
    max_A = max(A)
    min_A = min(A)
    output_array = []
    for i in range(0, len(A)):
        current_array = []
        if A[i] == max_A:
            end_index = i
            current_array.append(i)
            while end_index < len(A) or A[end_index] == min_A:
                end_index = +1
                current_array.append(i)
            current_array.append(A[end_index])
            if len(current_array) < len(output_array):
                output_array = current_array
        elif A[i] == min_A:
            start_index = i
            end_index = i
            current_array.append(i)
            while end_index < len(A) or A[end_index] == max_A:
                end_index = +1
                current_array.append(A[end_index])
            current_array.append(A[end_index])
            if len(current_array) < len(output_array):
                output_array = current_array
        print("Loop end",i)
    return output_array

solve([ 814, 761, 697, 483, 981 ])