class Solution(object):
    def isPalindrome(self, x):
        # Step 1: Handle edge cases
        # Negative numbers are not palindromes (e.g., -121 != 121-)
        # Numbers ending in 0 are not palindromes (e.g., 10 != 01), unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        left = x
        right = 0

        # Step 2: Reverse the second half of the number
        # We stop when left is no longer greater than right
        while left > right:
            # Shift right to the left and add the last digit of left
            right = (right * 10) + (left % 10)
            # Remove the last digit from left
            left = left // 10

        # Step 3: Check for both even and odd length numbers
        # Even: left == right (e.g., 12 == 12)
        # Odd: left == right // 10 (e.g., 1 == 12 // 10 removes the middle digit)
        return left == right or left == right // 10
