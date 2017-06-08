num=1001
prime= False
pfsqr= False
if num > 100 and num <100000:
 #if num<=1:
 #print("isn ot prime")
 if num>1:
  for i in range(2,num):
   if(num%i==0 and num !=i):
    break
  if num==i+1:
   prime = True
 for j in range(1,num+1):
  if num == j*j:
   pfsqr = True
 if prime == True and pfsqr == False:
  print ("FOO")
 if prime == False and pfsqr == True:
  print ("Bar")
 if prime == False and pfsqr == False:
  print ("FooBar")
