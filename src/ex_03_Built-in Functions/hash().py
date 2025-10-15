#What is hash()?
#The hash() function returns a unique integer value (called a hash value) for hashable objects.
#✅ Hashable objects are immutable — like:
#numbers (int, float)
#strings
#tuples (if they contain only hashable items)
#❌ Unhashable objects are mutable — like:
#lists
#sets
#dictionaries

print(hash(10))           # Hash of an integer
print(hash("Pooja"))      # Hash of a string
print(hash((1, 2, 3)))    # Hash of a tuple
