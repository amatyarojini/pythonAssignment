print ("Scores and Grades")
from random import randint
count = 1
while count<=10:
 score= randint(60,100)
 count+=1
 if score >= 60 and score <=69:
  grade="D"
 elif score >= 70 and score <=79:
  grade="C"
 elif score >= 80 and score <=89:
  grade="B"
 elif score >= 90 and score <=100:
  grade="A"
 print ("Score:",score,"Your grade is",grade)
