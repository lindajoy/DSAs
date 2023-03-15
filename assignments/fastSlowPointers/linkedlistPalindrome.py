"""
Determine whehther a linked list is a palindrome
"""

"""

Naive approach is converting the linked list to a normal array.
"""
def palindrome(head):
    nums = []

    while head:
        nums.append(head.data)
        head = head.next

        left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1

    return True


"""
Fast and slow pointers
"""

def isPalindrome(head):
    fast,slow = head, head


    # Find middle
    while fast and fast.next:
        fast = fast.next.next
        slow  = slow.next

    # reverse second half
    prev = None

    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # chek palindrome
    left,right = head, prev

    while right:
        if left.val != right.val:
            return False 

        left = left.next
        right = right.next

    return True


