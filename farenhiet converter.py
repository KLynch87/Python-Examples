#Temp Converter

temp = int(input("What is the temperature in Farenhiet?: "))
ctemp = (temp - 32)*5/9
print(temp,"coverts to","%3.1f" % ctemp, "degrees Celsius")

if temp < 32:
    print("Wow that's super cold!")
else:
    print("At least it's not freezing!")

input("\n\npress enter to end the program")
