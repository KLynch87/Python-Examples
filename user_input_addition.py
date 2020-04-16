# Trust Fund Buddy - Bad
# Demonstrates a logical error

print(
"""
            Trust Fund Buddy

Please enter the requested, monthly costs rounded up to whole dollar amount.

"""
)

car =  input("Lamborghini Tune-Ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")

