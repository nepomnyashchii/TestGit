import sys
import os

listOfParmas = sys.argv

if len(sys.argv) < 2:
    print("Give me directory name")
    sys.exit()

dir = sys.argv[1]

print("We are looking for " + dir)
if os.path.exists(dir):
    print("path exist")
else:
    print("path not exist")