def list_operations():
    my_list = [10, 20, 30, 40, 50]
    print("Original List:", my_list)

    my_list.append(60)
    print("After append:", my_list)

    my_list.insert(2, 25)
    print("After insert:", my_list)

    my_list.extend([70, 80, 90])
    print("After extend:", my_list)

    my_list.remove(30)
    print("After remove(30):", my_list)

    popped_element = my_list.pop(4)
    print("After pop(4):", my_list)
    print("Popped element:", popped_element)

    my_list.clear()
    print("After clear:", my_list)

    my_list = [10, 20, 30, 40, 50]
    print("Reinitialized List:", my_list)

    first_element = my_list[0]
    last_element = my_list[-1]
    print("First element:", first_element)
    print("Last element:", last_element)

    sliced_list = my_list[1:4]
    print("Sliced list (index 1 to 3):", sliced_list)

    my_list[2] = 35
    print("After modifying element at index 2:", my_list)

    index_of_40 = my_list.index(40)
    print("Index of 40:", index_of_40)

    count_of_50 = my_list.count(50)
    print("Count of 50:", count_of_50)

    my_list.sort()
    print("After sorting:", my_list)

    my_list.reverse()
    print("After reversing:", my_list)

list_operations()
