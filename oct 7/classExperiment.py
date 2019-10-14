# write program that converters miles to km

miles = input("Enter value for miles:")

km = float(miles) * 1.6

print("The conversion for", miles, "miles is", km, "km")

if km < 70:

    print("You are going too slow. The speed limit is 70 km")

elif km > 100:
    print("You are going too fast! The speed limit is 70 km")

else:

    print("Your speed is fine.")




