"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


def test(number):  # A function gets 1 value
    number = str(number)  # Set the number to be str
    return number == number[::-1]  # Return Ture/False if number is palindrome


print(test(131))
