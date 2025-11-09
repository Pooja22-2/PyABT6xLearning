#*FizzBuzz Test
#Write a program that prints 1 to 100
#For multiplies of **3**, print 'Fizz'
#For multiples of **5**, print 'Buzz'
#For multiples of **3** and **4** print both 'FizzBuzz'

for i in range(50):
    #Gives both O/P FizzBuzz
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
   # if i%3==0 and i%5==0: ---> gives wrong O/P only execute first condition and print Fizz not Buzz
        #print("FizzBuzz")
    else:
        print(i)

