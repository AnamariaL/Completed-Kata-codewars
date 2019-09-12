"""Description:
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.

In Racket, the function is called palindrome?

(palindrome? "nope") ; returns #f
(palindrome? "Yay")  ; returns #t
"""
def is_palindrome(s):
    return True if s.lower() == s.lower()[::-1] else False