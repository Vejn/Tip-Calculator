#Simple project, creating the tip calculator based on your satisfaction with the service

#Printing the welcome message
print("Hello! I hope you enjoyed the meal!")
print("Now is time to calculate the tip")

#Asking for user input
bill = float(input("How much is the bill?: "))
num_persons = int(input("How many people are sharing the bill?: "))
service = int(input("How would you rate service(1 - 10): "))

#Calculating tip based on happiness
tip = 0.1

if service < 2:
  tip = 0.05
elif service < 5:
  tip = 0.1
elif tip < 8:
  tip = 0.12
else:
  tip = 0.15

#Splitting bill per person
tip_per_person = ((bill* tip)) / num_persons
total_per_person = (bill/num_persons) + tip_per_person

#Printing result
print(f"Each of you should give {round(tip_per_person,2)} tip!")
print(f"Each should pay {round(total_per_person,2)} total!")