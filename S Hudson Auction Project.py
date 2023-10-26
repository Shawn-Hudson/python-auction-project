def loadBidding(price):
  bid = 0
  
  while bid < price:
        print(f"The minimum bid is ${price}\n")

        answer = input("Would you like to place a bid? (y/n)\n")

        if answer == 'y':
            bid = int(input("\nWhat is your bid? "))
            
        else:
            print("\nGoodbye!\n")
            break  

        print(f"\nPlaced bid is ${bid}.\n")

        if bid >= price:
          print("You won the item!\n")
          print("Please pay for your item within 24 hours\n")
        else:
          print("You lost the item! :(\n")
          break
          
        payment_method = input("Would you like to pay with cash or credit? (c/d):")

        if payment_method == 'c':
          print("Please pay with cash within 24 hours\n")
        elif payment_method == 'd':
         print("Please pay with credit within 24 hours\n")
        else:
          print("Invalid payment method. Please try again.\n")
          continue
          

price = 0

print("Let's list an Item for sale")
price = int(input("What is the price of the item?\n\n"))

item = input("\nWhat is the name of your item?\n")

print(f"\nListed the price of {item} for ${price}\n")

loadBidding(price)