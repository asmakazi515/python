def dictionary_operations():
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print("Original Dictionary:", my_dict)

    my_dict["email"] = "alice@example.com"
    print("After adding key-value pair:", my_dict)

    my_dict["age"] = 31
    print("After modifying value for 'age':", my_dict)

    removed_value = my_dict.pop("city")
    print("After pop('city'):", my_dict)
    print("Removed value:", removed_value)

    popped_item = my_dict.popitem()
    print("After popitem():", my_dict)
    print("Popped item:", popped_item)

    age_value = my_dict.get("age")
    print("Value for 'age':", age_value)

    name_value = my_dict.get("name", "Not Found")
    print("Value for 'name':", name_value)

    my_dict.update({"country": "USA", "language": "English"})
    print("After update:", my_dict)

    keys = my_dict.keys()
    print("Keys:", keys)

    values = my_dict.values()
    print("Values:", values)

    items = my_dict.items()
    print("Items:", items)

    my_dict.clear()
    print("After clear:", my_dict)

    my_dict = {"name": "Bob", "age": 25}
    print("Reinitialized Dictionary:", my_dict)

    print("Length of dictionary:", len(my_dict))

dictionary_operations()
