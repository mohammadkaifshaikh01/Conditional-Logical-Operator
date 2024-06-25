def check_speed(distance,time):
   speed = distance / time

   if speed > 40:
      print("Apply Brakes")
   else:
      print("Keep Going")

distance = 100
speed = 2
check_speed(distance,speed)