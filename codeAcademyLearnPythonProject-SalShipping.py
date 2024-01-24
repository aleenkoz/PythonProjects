weight= 4.8
cost=0
#ground shipping
if weight<=2:
  cost= weight*1.50
  print("Shipping  will cost you: ")
  print(cost)
elif weight>2 and weight<=6:
  cost= weight*3.00
  print("Shipping  will cost you: ")
  print(cost)
elif weight>6 and weight<=10:
  cost= weight*4.00
  print("Shipping  will cost you: ")
  print(cost)
else:
  cost= weight*4.75
  print("Ground Shipping will cost you: ")
  print(cost)

cost_premium=125.00
print("Premium Shipping will cost you: ")
print(cost_premium)

#drone shipping
cost_drone=0
if weight<=2:
  cost_drone= weight*4.50
elif weight>2 and weight<=6:
  cost_drone= weight*9.00
elif weight>6 and weight<=10:
  cost_drone= weight*12.00
else:
  cost_drone= weight*14.25

print("Drone Shipping will cost you: ")
print(cost_drone)