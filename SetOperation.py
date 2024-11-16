def set_operations():
    my_set = {10, 20, 30, 40, 50}
    print("Original Set:", my_set)

    my_set.add(60)
    print("After add:", my_set)

    my_set.remove(30)
    print("After remove(30):", my_set)

    my_set.discard(70)
    print("After discard(70):", my_set)

    popped_element = my_set.pop()
    print("After pop:", my_set)
    print("Popped element:", popped_element)

    my_set.clear()
    print("After clear:", my_set)

    my_set = {10, 20, 30, 40, 50}
    another_set = {30, 40, 50, 60, 70}

    union_set = my_set | another_set
    print("Union:", union_set)

    intersection_set = my_set & another_set
    print("Intersection:", intersection_set)

    difference_set = my_set - another_set
    print("Difference:", difference_set)

    symmetric_difference_set = my_set ^ another_set
    print("Symmetric Difference:", symmetric_difference_set)

    print("Length of set:", len(my_set))

set_operations()
