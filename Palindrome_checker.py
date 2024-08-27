import string

def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    reversed_s = cleaned_s[::-1]
    return cleaned_s == reversed_s


input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f' "Palindrome" ')
else:
    print(f' "Not a palindrome" ')
