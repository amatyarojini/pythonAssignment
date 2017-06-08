import random
numoftoss = 0
numofheads = 0
numoftails = 0
while numoftoss <5000:
 x=random.uniform(0,1)
 numoftoss+=1
 rounded_x = round(x)
 if rounded_x==1:
  numofheads+=1
  print ("Attempt #",numoftoss,"Throwing a coin...It's a head Got",numofheads," heads So far  and ",numoftails,"tails So far")
 elif rounded_x==0:
  numoftails+=1
  print ("Attempt #",numoftoss,"Throwing a coin...It's a tail Got",numoftails," tails So far and ",numofheads,"heads So far")
print ("End of program Thankyou!!!")
