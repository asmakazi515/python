import re

def regex_examples(text):
    print("Original Text:")
    print(text)
    print("\n")

    # 1. Match all digits (e.g., phone numbers, amounts)
    print("1. Match all digits:")
    digits = re.findall(r'\d+', text)
    print(digits)
    print("\n")

    # 2. Match words (alphanumeric strings without spaces)
    print("2. Match all words:")
    words = re.findall(r'\b\w+\b', text)
    print(words)
    print("\n")

    # 3. Match specific patterns (email addresses)
    print("3. Match all email addresses:")
    emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}', text)
    print(emails)
    print("\n")

    # 4. Match dates in format dd-mm-yyyy (example: 12-05-2024)
    print("4. Match dates in dd-mm-yyyy format:")
    dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
    print(dates)
    print("\n")

    # 5. Replace numbers with a placeholder text
    print("5. Replace all numbers with '[NUMBER]':")
    replaced_text = re.sub(r'\d+', '[NUMBER]', text)
    print(replaced_text)
    print("\n")

    # 6. Match a URL (basic version)
    print("6. Match all URLs:")
    urls = re.findall(r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,6}', text)
    print(urls)
    print("\n")

    # 7. Match a word at the beginning of a line (case-insensitive)
    print("7. Match a word at the beginning of a line:")
    line_start_word = re.findall(r'^[A-Za-z]+', text, re.M)  # re.M allows matching at the beginning of each line
    print(line_start_word)
    print("\n")

    # 8. Match any whitespace character (spaces, tabs, etc.)
    print("8. Match all whitespace characters:")
    whitespace_chars = re.findall(r'\s', text)
    print(len(whitespace_chars))  # Printing number of whitespace characters
    print("\n")

    # 9. Match non-word characters (symbols, punctuation)
    print("9. Match all non-word characters:")
    non_words = re.findall(r'\W', text)
    print(non_words)
    print("\n")

    # 10. Match a phone number (simple example for US-style: (xxx) xxx-xxxx)
    print("10. Match phone numbers (simple US format):")
    phone_numbers = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}', text)
    print(phone_numbers)
    print("\n")

    # 11. Match a hexadecimal number (e.g., 0xABC123)
    print("11. Match hexadecimal numbers:")
    hex_numbers = re.findall(r'0x[a-fA-F0-9]+', text)
    print(hex_numbers)
    print("\n")

    # 12. Extract the first word in the text
    print("12. Extract the first word:")
    first_word = re.match(r'\b\w+\b', text)
    print(first_word.group() if first_word else "No word found")
    print("\n")

# Example input text containing various patterns
sample_text = """
John's email is john.doe@example.com, and his phone number is (123) 456-7890.
You can also contact him via his alternate email: johndoe123@anothermail.org.
His favorite color is #FF5733, and his address is 1234 Elm St., Springfield.
Check out his website at http://www.johndoe.com or visit the online store at https://shop.johndoe.com.
The event is on 12-05-2024, and tickets cost 200 dollars.
For inquiries, call 800-555-1212 or email support@johndoe.com.
"""

# Run all regex examples on the sample text
regex_examples(sample_text)
