expensesList = []
print(" Welcome to Expense Tracker Khrcha kam kiya karo ")

while True:
 print("===MENU===")
 print("1. Add Expense")
 print("2. View all Expenses")
 print("3. View Total Khrcha")
 print("4. Exit")

 select=int(input("Enter your choice:"))


 if(select == 1):
  date= input("Kis date par khrcha kiya tha?: ")
  category= input("Kis type ka khrcha kiya? (Food, Travel, Makeup, Books): ")
  description= input("Aur detail dedo: ")
  amnt= float(input("Enter the amount: "))

  expense= {
    "date": date,
    "category": category,
    "description": description,
    "amnt": amnt
  }

  expensesList.append(expense)
  print(" Done bro. Expense added successfully!")


 elif (select == 2):
  if(len (expensesList)==0):
    print("No Expenses Added. Jao pehle khrcha karo. ")
  else:
    print("==== Ye y apka sara expense ====")
    count= 1
    for eachKharcha in expensesList:
         print(f"Kharcha Number: {count}, Date: {eachKharcha["date"]}, Category: {eachKharcha["category"]}, Description: {eachKharcha["description"]}")
         count= count+1


 elif(select == 3):
  total= 0
  for eachKharcha in expensesList:
   total = total + eachKharcha ["amnt"]

  print("\n TOTAL KHRCHA = ", total)


 elif (select == 4):
  print("Dhanyawad aapne humara system use kiya")
  break
 else:
  print("INVALID CHOICE. TRY AGAIN")
