string_input = 'abcd'
output = []
# get individual element
string_element = []
for ele in string_input:
    string_element.append(ele)


def add_suffix(list_input, ele):
    print(list_input)
    print(ele)
    temp_list = []
    for input_ele in list_input:
        temp_list.append(input_ele + ele)
    print(temp_list)
    list_input = list_input + temp_list
    return list_input

output.append(string_element[0])
for ele in string_element[1:]:
    output = add_suffix(output, ele)

print(output)
