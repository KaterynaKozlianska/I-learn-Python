# TASK:
#  Nonzero number of values ​​- command line arguments. 
#   Values-arguments can be numbers or strings that consist of numbers and letters of the Latin alphabet without spaces.
#  The row consists of the values obtained in reverse order with spaces

import sys
x=str(sys.argv[1:])
if len(sys.argv)>1:
 x=(x[2:(len(x)-2):1])
 x=list(x)
 x.reverse()
 x=str(x)
 x=x.replace("'","").replace(",","").replace("[","").replace("]","")
 print (x)
else:
 print ('Please input more then zero numbers')