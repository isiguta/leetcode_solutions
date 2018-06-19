# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


def add_two_numbers(l1, l2):
    l1_values = ''
    while l1 is not None:
        l1_values = l1_values + str(l1.val)
        l1 = l1.next

    l2_values = ''
    while l2 is not None:
        l2_values = l2_values + str(l2.val)
        l2 = l2.next

    result = int(l1_values[::-1]) + int(l2_values[::-1])

    return [int(d) for d in str(result)[::-1]]
