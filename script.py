def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50
  elif weight <= 6:
    cost = 3.00
  elif weight <= 10:
    cost = 4.00
  else:
    cost = 4.75
  return 20.00 + (cost * weight)

#print(ground_shipping(8.4))

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50
  elif weight <= 6:
    cost = 9.00
  elif weight <= 10:
    cost = 12.00
  else:
    cost = 14.25
  return (cost * weight)
#print(drone_shipping(1.5))

def cheap_shipping(weight):
 ground = (ground_shipping(weight))
 premium = premium_ground_shipping
 drone = (drone_shipping(weight))

 if ground < premium and ground < drone:
    shipping = "Standard shipping"
    cost = ground
 elif premium < ground and premium < drone:
    shipping = "Premium Shipping"
    cost = premium
 else:
    shipping = "Drone Shipping"
    cost = drone
    

print("You should ship using " + shipping + " and the total will be $" + cost)
  
print(cheap_shipping(4.8))  
print(cheap_shipping(41.5))