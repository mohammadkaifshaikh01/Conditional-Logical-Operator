def check_fuel_distance(fuel , distance):

   result = fuel * distance

   if result > 50:
      print("Enough")
   else:
      print("Go On")


fuel = 1
distance = 46
check_fuel_distance(fuel , distance)