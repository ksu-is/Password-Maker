import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symobls = "@#$%&*+!"


upper, lower, nums, syms = True, True, True, True


all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums: 
    all += digits
if syms:
    all += symobls


length = 5
amount = 2


for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
