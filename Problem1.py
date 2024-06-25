def update_Compare(num1,num2,num3):

   if num1 > num2:
      print("True")
   else:
      print("False")

   num1 = num1 + num3

   if num1 > num2:
      print("True")
   else:
      print("False")

num1,num2,num3 = map(int,input().split())
update_Compare(num1,num2,num3)