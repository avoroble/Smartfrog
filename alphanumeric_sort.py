import re

def alphanumeric_sort(input_string):
    # Split input into chunks of numbers and non-numbers
    chunks = re.findall(r'\d+|[^\d]', input_string)

    # Separate into groups
    numbers = []
    lowercase_letters = []
    uppercase_letters = []
    others = []

    for chunk in chunks:
        if chunk.isdigit():
            numbers.append(int(chunk))  # Treat as integers for correct sorting
        elif chunk.islower():
            lowercase_letters.append(chunk)
        elif chunk.isupper():
            uppercase_letters.append(chunk)
        else:
            others.append(chunk)

    # Sort each group
    numbers.sort()
    lowercase_letters.sort()
    uppercase_letters.sort()
    others.sort()

    # Combine all sorted groups
    sorted_result = ''.join(
        [str(num) for num in numbers] + lowercase_letters + uppercase_letters + others
    )

    return sorted_result

# Request input from the user
input_str = input("Enter a string to sort alphanumerically: ")

# Call the function and print the result
output = alphanumeric_sort(input_str)
print("Sorted output:", output)