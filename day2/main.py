#greeting
print("Welcome to the tip calculator")

#taking input from user
bill = input("Enter your total bill: ")
percentage= input("Enter the percentage you want to tip: ")
peoples= input("Enter the total number of peoples: ")

#calulating bill after tip
tip=float(bill)/100*float(percentage)
total_bill=float(bill)+tip
per_person=total_bill/int(peoples)
per_person=round(per_person,2)
per_person="{:.2f}".format(per_person)

#printing the bill
print(f"Each person should pay: {per_person} ")
