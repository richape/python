def is_palindrome(s):
    if s == s[::-1]: #This checks if the original string s is equal to its reversed version s[::-1].

        return True
    else: 
        return False

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("madam"))    # True
print(is_palindrome("foolish"))  # False

# s[::-1] is a slicing operation that reverses the string s.
# The expression s == s[::-1] checks if s is equal to s[::-1].

# If the condition s == s[::-1] is True (i.e., the string is the same forward and backward), the function returns True.
# If the condition is False (i.e., the string is not the same forward and backward), the function returns False.

# Simplified function:
# def is_palindrome(s):
#     return s == s[::-1]
# This version does the same thing but is more concise. The comparison s == s[::-1] evaluates to True or False, which is directly returned.