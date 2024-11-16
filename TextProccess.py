import re


text = """
Hello, world! Welcome to Python programming. Python is great for text processing.
Let's explore text processing in Python. Python, Python, Python!
"""

# 1. Clean up the text (remove punctuation)
cleaned_text = re.sub(r'[^\w\s]', '', text)  
print("Cleaned Text:")
print(cleaned_text)
print("\n")

# 2. Count occurrences of the word 'Python'
python_count = len(re.findall(r'\bPython\b', cleaned_text))
print(f"Count of 'Python': {python_count}")
print("\n")

# 3. Replace 'Python' with 'Programming'
replaced_text = re.sub(r'\bPython\b', 'Programming', cleaned_text)
print("Text After Replacement:")
print(replaced_text)
print("\n")

# 4. Convert the entire text to lowercase
lowercase_text = cleaned_text.lower()
print("Lowercase Text:")
print(lowercase_text)
