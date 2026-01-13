class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # For any n >= 4, n in base (n-2) is always "12" which is not palindromic
        # Therefore, no number >= 4 is strictly palindromic
        return False