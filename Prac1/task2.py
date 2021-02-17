def list_sort(list_to_sort):
    return sorted(list_to_sort)

input_list = [float(number) for number in input().split(' ')]

sorted_list = list_sort(input_list)

print(sorted_list)