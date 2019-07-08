#  TASK:
# The string is passed to the program as a command line argument. 
#It may contain spaces, letters of the Latin alphabet in any case and numbers. 
# "YES" if the resulting string is a palindrome, or "NO" - if not.

import sys
x=str(sys.argv[1:])
flag=True
x_cleaned=x.lower().replace(" ","").replace("'","").replace(",","").replace("[","").replace("]","")
x_length =len(x_cleaned)
for i in range(x_length//2):
 if x_cleaned[i]!=x_cleaned[(x_length-1)-i]:
  flag=False	
if flag: 
 print ('YES')
else:
 print ('NO')