#Used in dynamic code generation or testing.
#Executes a string of Python code (not just expressions like eval()).
code="""
for i in range(3):
    print("Hello", i)
"""
exec(code)
