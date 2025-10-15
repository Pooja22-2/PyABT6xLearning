#The divmod() function in Python is a built-in function that returns both the quotient and the remainder of a division in one step.
#10 ÷ 3 = 3 (quotient)
#10 % 3 = 1 (remainder)
#So, divmod(10, 3) → (3, 1)

#divmod(a, b)
#a → dividend (the number to be divided)
#b → divisor (the number you divide by)

#Basic Example
#result = divmod(10, 3)
#print(result)

#divmod()
print(divmod(10, 3))   # (3, 1)
q, r = divmod(25, 4)
print("Quotient:", q)
print("Remainder:", r)