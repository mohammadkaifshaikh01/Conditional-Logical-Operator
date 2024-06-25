def sum_compare(one,two,three,four,five):

   num1 = one+two+three
   num2 = four+five

   if num1 > num2:
      print("true")
   else:
      print("false")


one,two,three,four,five = map(int,input().split())
sum_compare(one,two,three,four,five)