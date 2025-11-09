#Q - Create a function which will take a positive number from the user and perform square of the number?

def num():
    n = int(input("Enter a positive number: "))
    if n>0:
        print("Square ofa number is:",n**2)
    else:
        print("Enter a positive number")

num()