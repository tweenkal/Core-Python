# 👉Keyword :- 1)Break 2)Continue 3) Pass

# 👉1)break :- means the jump out of the loop

av = 5

x = int(input("How many candy you want?="))

i = 1

while i <= x:
    if i > av:
        print("Out of the stock")
        break
    print("candy",i)
    i += 1

print("bye")

# 👉Continue :- it is not jump out the loop it is only skip the
# remaining statements.

# 👉print the 1 to 100 number but is not print the divisible by 3 or 5
# then is skip and continue for the loop

for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        continue

    print(i)


# 👉Pass:-Pass statement in Python is a null operation or a placeholder.
# It is used when a statement is syntactically required but we don’t
# want to execute any code. It does nothing but allows us to maintain
# the structure of our program.

for i in range(1,101):
    if i % 2 != 0:
        pass
    else:
        print(i)