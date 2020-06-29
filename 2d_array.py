input = [[-9, -9, -9, 1, 1, 1],
         [0, -9, 0, 4, 3, 2],
         [-9, -9, -9, 1, 2, 3],
         [0, 0, 8, 6, 6, 0],
         [0, 0, 0, -2, 0, 0],
         [0, 0, 1, 2, 4, 0]]
input = [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 2, 4, 4, 0],
         [0, 0, 0, 2, 0, 0],
         [0, 0, 1, 2, 4, 0]]

largest = input[0][0] + input[0][1] + input[0][2] + input[1][1] + input[2][0] + input[2][1] + input[2][2]
for index_row in range(0, 5):
    for index_col in range(0, 5):
        if index_row + 1 > 5 or index_row + 2 > 5 or index_col + 1 > 5 or index_col + 2 > 5:
            continue
        else:
            start_row = input[index_row][index_col] + input[index_row][index_col + 1] + input[index_row][index_col + 2]
            print("start row",start_row)
            column_val = input[index_row + 1][index_col + 1]
            print("Column value",column_val)
            end_row = input[index_row + 2][index_col] + input[index_row + 2][index_col + 1] + input[index_row + 2][
                index_col + 2]
            print("End row",end_row)
            temp = start_row + column_val + end_row
            print("The temp is",temp)
            if temp > largest:
                largest = temp

print("The largest is", largest)
