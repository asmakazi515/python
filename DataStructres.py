from collections import deque

# 1. Using Lists
def list_example():
    print("List Example:")
    # Create a list
    my_list = [10, 20, 30, 40, 50]
    
    # Add elements
    my_list.append(60)  
    my_list.insert(2, 25)  
    # Remove elements
    my_list.remove(40)  
    popped_value = my_list.pop() 
    print(f"Modified List: {my_list}, Popped Value: {popped_value}")
    print("\n")

# 2. Using Tuples
def tuple_example():
    print("Tuple Example:")
    my_tuple = (1, 2, 3, 4, 5)
    
    # Access elements
    first_element = my_tuple[0]
    
    print(f"First element: {first_element}")
    print(f"Full Tuple: {my_tuple}")
    print("\n")

# 3. Using Dictionaries
def dictionary_example():
    print("Dictionary Example:")
    # Create a dictionary
    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    # Add or modify an entry
    my_dict["age"] = 31 
    my_dict["email"] = "alice@example.com"  
    
    # Access a value by key
    name = my_dict.get("name")
    
    # Remove a key-value pair
    city = my_dict.pop("city")
    
    print(f"Modified Dictionary: {my_dict}")
    print(f"Removed 'city': {city}")
    print(f"Name: {name}")
    print("\n")

# 4. Using Sets
def set_example():
    print("Set Example:")
    # Create a set (unique values)
    my_set = {10, 20, 30, 40, 50}
    
    # Add and remove elements
    my_set.add(60)  
    my_set.remove(20)  
    
    # Sets automatically remove duplicates
    my_set.add(30)  
    
    print(f"Modified Set: {my_set}")
    print("\n")

# 5. Using Queues (with deque from collections)
def queue_example():
    print("Queue Example (using deque):")
    queue = deque()
    
    # Add elements to the queue
    queue.append("First")
    queue.append("Second")
    queue.append("Third")
    
    # Remove elements from the queue (FIFO)
    first_out = queue.popleft()
    second_out = queue.popleft()
    
    print(f"Queue after enqueue and dequeue: {queue}")
    print(f"First out: {first_out}, Second out: {second_out}")
    print("\n")

# Main function to run all examples
if __name__ == "__main__":
    list_example()
    tuple_example()
    dictionary_example()
    set_example()
    queue_example()
