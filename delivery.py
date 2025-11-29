def calculate_delivery_fee(amount,distance):
   try:
      amount= int(input('enter the amount in:(ksh'))
      distance= int(input("enter the distance:(km)"))
      fee= calculate_delivery_fee(amount,distance)
        
    

      if amount < 0 and distance < 0:
        raise ValueError("amount and distance cannot be zero")
      if amount >= 500:
        return 0
      if distance <= 5:
        return 50
      if distance <= 15:
        return 100
      else:
        return 150
    

 amount = int(input("enter the amount in:(kshs)"))
    distance = int(input("enter the distance in: (km)")) 
     fee = calculate_delivery_fee(amount,distance)
     print(f"delivery fee:kshs{fee}")
except (ValueError) as e:
    print(f"error :{e}")

   