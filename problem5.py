def area_parameter(l1,b1,l2,b2):
   areaofrectangle = l1*b1
   areaofrectangle2 = l2*b2

   periofrectangle = 2*(l1+b1)
   periofrectangle2 = 2*(l2+b2)

   if areaofrectangle > areaofrectangle2 :
      print("True")
   else:
      print("False")

   if periofrectangle > periofrectangle2:
      print("True")
   else:
      print("False")


l1,b1,l2,b2= map(int,input().split())
area_parameter(l1,b1,l2,b2)
