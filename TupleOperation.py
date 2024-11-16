def tuple_operations():
    my_tuple = (10, 20, 30, 40, 50)
    print("Original Tuple:", my_tuple)

    new_tuple = my_tuple + (60,)
    print("After concatenation:", new_tuple)

    sliced_tuple = my_tuple[1:4]
    print("Sliced tuple (index 1 to 3):", sliced_tuple)

    count_of_30 = my_tuple.count(30)
    print("Count of 30:", count_of_30)

    index_of_40 = my_tuple.index(40)
    print("Index of 40:", index_of_40)

    print("Length of tuple:", len(my_tuple))

tuple_operations()
