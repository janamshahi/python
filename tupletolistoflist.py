def convert_tuples_to_lists(tuple_list):
    return [list(t) for t in tuple_list]
original_list1 = [(1, 2), (2, 3), (3, 4)]
converted_list1 = convert_tuples_to_lists(original_list1)
print("Original list of tuples:", original_list1)
print("Converted list of lists:", converted_list1)

original_list2 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
converted_list2 = convert_tuples_to_lists(original_list2)
print("\nOriginal list of tuples:", original_list2)
print("Converted list of lists:", converted_list2)
