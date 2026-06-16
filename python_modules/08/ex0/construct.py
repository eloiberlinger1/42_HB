import sys

print(sys.executable)
print()
print(sys.version)
print()
print(sys.prefix)
print()

if (sys.prefix != sys.base_prefix):
    print("You are in a virtal environment")
else:
    print("You are not in a virtal environment")
