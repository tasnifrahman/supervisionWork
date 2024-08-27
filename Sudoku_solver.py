def is_palindrome(s):
    return s == s[::-1]

def show_palindromic_substrings(s):
    n = len(s)
    palindromic_substrings = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromic_substrings.add(substring)

    sorted_palindromic_substrings = sorted(list(palindromic_substrings))
    return sorted_palindromic_substrings


input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

palindromic_substrings = show_palindromic_substrings(input_string)
print("Palindromic substrings are:")
for substring in palindromic_substrings:
    print(substring)

