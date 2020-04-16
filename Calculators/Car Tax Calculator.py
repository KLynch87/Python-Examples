#Car Salesman program

car_price = int(input("What is the base price of the car?: "))
tax = .1
license = .1
dealer_prep = 100
destination_charge = 50

print("The final price of your car would be: ",(car_price*tax) + (car_price*license) + dealer_prep + destination_charge + car_price)

input("\n\nPress the enter key to exit.")
