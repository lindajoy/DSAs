"""
Problem

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""
# 💡 Modulous operation  => Mistake with this answer is that it does not return a list
def _fizzbuzz(n):
    for i in range(1, n+1):
        if i%5 == 0 and i%3 == 0:
            print(i,'FizzBuzz')
        elif i%3 == 0:
            print(i,'Fizz')
        elif i%5 == 0:
            print(i,'Buzz')
        else:
            print(str(i))

#_fizzbuzz(15)
#_fizzbuzz(3)
#_fizzbuzz(5)

"""
Something I have learnt is since the above function does not return anything printing the fizzbuzz fn will return NONE
If you find yourself, appending a list inside a for-loop, Its a good idea to use a a list comprehension instead.

  1. What are the inputs ?
      An integer
"""
fizz_int = 3

def _fizzbuzz2(i):
    if i%5 == 0 and i%3 == 0:
        return 'Fizzbuzz'
    elif i%3 == 0:
        return 'Fizz'
    elif i%5 == 0:
        return'Buzz'
    else:
        return str(i)

final_Strings = [_fizzbuzz2(i) for i in range(1, fizz_int + 1)]
print('Here are the final strings:', final_Strings)




