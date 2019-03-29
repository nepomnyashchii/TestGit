import sys
print (sys.argv)

# import sys
# listOfParmas = sys.argv

# for arg in listOfParmas:
#     print(arg)

import sys
if len(sys.argv)>1:
    for arg in sys.argv [1:]:
        print(arg)
else:
    print ("No argument provide")