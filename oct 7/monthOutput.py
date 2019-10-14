month = input("Enter month: ")


if month.lower() == "January" or month.lower() == "january" or month.lower() == "February" or month.lower() == "february" or month.lower() == "March" or month.lower() == "march" or month.lower() == "April" or month.lower() == "april" :
    print("Winter")

elif month.lower() == "May" or month.lower() == "may" or month.lower() == "June" or month.lower() == "june" or month.lower() == "July" or month.lower() == "july" or month.lower() == "August" or month.lower() == "august":
    print("Summer")

elif month.lower() == "September" or month.lower() == "september" or month.lower() == "October" or month.lower() == "october" or month.lower() == "November" or month.lower() == "november" or month.lower() == "December" or month.lower() == "december":
    print("Fall")

else:
    print("Thats not a month!!")

