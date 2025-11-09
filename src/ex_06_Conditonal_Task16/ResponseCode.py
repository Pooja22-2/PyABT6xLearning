#Write an if-else block to check whether the response is successful (status code 200) or not.
response=int(input("Enter Response code:\n"))
if response==200:
    print("Passed API Request")
else:
    print("Failed API Response")