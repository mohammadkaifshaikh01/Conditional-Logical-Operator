def sevenNumber(a,b,c,d,e,f,g):

   sum1 = (a+b)*c
   sum2 = d+e+f+g

   if sum1 > sum2:
      print("True")
   else:
      print("False")



a,b,c,d,e,f,g = map(int,input().split())
sevenNumber(a,b,c,d,e,f,g)