# 1. Writing to a file
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# 2. Reading from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# 3. Appending to a file
def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print(f"Content successfully appended to {filename}")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Example usage
if __name__ == "__main__":
    filename = "sample.txt"
    initial_content = "This is the initial content of the file.\n"
    append_content = "This is the appended content.\n"
  
    write_to_file(filename, initial_content)
    
  # Reading from the file
    read_from_file(filename)
    
    # Appending to the file
    append_to_file(filename, append_content)
    
    # Reading the updated file content
    read_from_file(filename)
