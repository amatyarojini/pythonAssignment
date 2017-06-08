l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
l = ['magical','unicorns']
sumInt= 0
allString = ""
num=len(l)
for i in l:
  result1=isinstance(i, int)
  if result1 == False:
    for j in l:
      result2=isinstance(j, str)
      if result2 == False:
        break
    if result2 == True:
     print ("The array you entered is of string type")
     for count in range(0,num):
      allString+=l[count]
     print ("String:",allString)

    elif result2 == False:
     print ("The array you entered is of mixed type")
    break

if result1 == True:
 print ("The array you entered is of integer type")

 for count in range(0,num):
  sumInt+=l[count]
 print (sumInt)
