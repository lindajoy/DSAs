"""
Reverse Digits: Write a program which takes an integer and returnd the integer corresponding to the digits of the input
written in reverse order.  For example, the reverse of 42 is 24, and the reverse of -314 is -413.
"""
num = 42

# Time Complexity: The time complexity is O(n) where n is the number of digits in k

def reverse_number(num):
    reversed = 0
    abs_num = abs(num)

    while abs_num:
        digit = abs_num % 10
        reversed = reversed * 10 + digit
        # reversed = 2
        abs_num = abs_num // 10

    return -reversed if num < 0 else reversed

print(reverse_number(42))
print(reverse_number(314))
print(reverse_number(411))
print(reverse_number(-411))

# 💡 What if the number is negative? My solution above would not work.
# Same solution done differently!
def reverse_all_kinda_numbers(num):
    result, x_remaining = 0, abs(num)

    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10

    return -result if num < 0 else result

   