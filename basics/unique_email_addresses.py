"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. 
Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. 
This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], 
return the number of different addresses that actually receive mails.

Input:  emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
"""

# Whats the input: An array of email strings
# Whats the ouput: Number of addresses that will recieve the email.

# Hehe, Kumbe it was not that difficult.

# Take away: I have learnt more about string manipulation
# 💡 I found this question intersting

def unique_email_addresses(emails):
    my_dict = set()

    for e in emails:
        local, domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        my_dict.add((local, domain))
    return len(my_dict)

print(unique_email_addresses(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


# Something useful learnt today was:
# With split you are converting a string's element to a list.

sample_email = "test.email+alex@leetcode.com"
print(sample_email.split("@"))
random_list = sample_email.split("@")
print(random_list[0].split('+')[0])

# Say you had something like
phone_number = "123-456-789"
print(phone_number.split('-'))

some_message = "Hello Joy You are doing pretty Good"
print(some_message.lower().split(" "))

# Some random list
lst1 = [1,2,3,4,5]
prod = 1

for i in lst1:
    prod = prod * i
print(prod)

print(type(2))
print(int("-2"))


def calPoints( operations) -> int:
    ops = []
    for i in operations:
        if i == "D":
            number = (ops[-1]) * 2
            ops.append(number)
        elif i == "C":
            ops.pop(-1)
        elif i == "+":
            lastTwonumbers = ops[-2:]
            totalsum = sum(lastTwonumbers)
            ops.append(totalsum)
        else:
            integer = int(i)
            ops.append(integer)

    # 5 + -2 + -4 + 9 + 5 + 14 = 27.
    print(ops)
    return sum(ops)


print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))

[5, -2, -4, 9,]