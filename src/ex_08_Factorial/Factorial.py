num=int(input("Enter a num which Fact you want to enter"))
fact=1
if num<=1:
    print("The factorial of ",num,"is ",fact)
else:
    for i in range (1,num+1):
        fact=fact*i
    print("The factorial of ",num," is ",fact)

