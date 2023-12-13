# Break statement in Python terminates the loop containing it.

for num in range(0, 10):
    if num == 5:
        break

    print(f'Iteration: {num}')

# Hmm..
for chance in range(1,4):
    password = input("\n Enter a password:")
    if password == "Python":
        print("🤟🏼 Correct Password\n 🎉 Unlocking Your Phone")
        break
    print(f"Incorrect attempt: You have {chance} remaining")

# Continue: Statement is used to skip the remaining code inside a loop for the current iteration only
for i in range(5):
    if i == 3:
        continue
    print('Boom🤔',i)

for num in range(0,10):
    if num == 5:
        continue
    print(f"iteration: {num}")

# Pass statement: The pass statement does nothing

for num in range(0, 10):
    if num == 5:
        pass

    print(f'iteration:{num}')