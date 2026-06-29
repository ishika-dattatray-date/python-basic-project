

def analyze_string(s):
    # Empty string check
    if s == "":
        print("String is empty")
        return

    # Length of string
    print("Length of string:", len(s))

    # Reverse string
    print("Reverse string:", s[::-1])

    # Count vowels
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    print("Number of vowels:", count)

    # Print characters with positive and negative index
    print("Characters with index:")

    for i in range(len(s)):
        print(s[i], "Positive index:", i, "Negative index:", i-len(s))


# User input
text = input("Enter a string: ")

# Function call
analyze_string(text)