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

# Рядок, передається в програму як аргумент командного рядка. Може містити пробіли, літери латинського алфавіту в будь-якому регістрі та цифри. 
# Рядок "YES", якщо отриманий рядок є паліндромом, або "NO" - якщо ні. 