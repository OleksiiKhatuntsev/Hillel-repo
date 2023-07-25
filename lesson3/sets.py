# set_example = {"test_value", 1, 2, False, False}
#
# print(set_example)
# print(set_example[0])


list_example = ["DUPLICATE", "DUPLICATE", "NEW VALUE", 2]
set_from_list = list(set(list_example))
print(list_example)
print(set_from_list)
tuple_from_list = tuple(list_example)
print(tuple_from_list)
# print(dict(list_example))
list_from_set = list(set_from_list)
print(list_from_set)
print(list("asd"))