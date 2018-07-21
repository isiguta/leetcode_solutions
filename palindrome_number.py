# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Could you solve it without converting the integer to a string?


def is_palindrome(x):

    if x < 0:
        return False
    div = x
    mods = []

    # getting each digit from the number
    while div != 0:
        div, mod = divmod(div, 10)
        mods.append(mod)

    # check if the number is palindromic. See Wikipedia for detailed explanation from math viewpoint.
    for i in range(0, len(mods)):
        if mods[i] != mods[len(mods) - i - 1]:
            return False

    return True

