# Gets first and last name
first_name = input("what's your first name ")
last_name = input("what's your last name or your mother's maiden name? " )

#prints first and last name
print("Cool name!", "I'll refer to you as: ", last_name, first_name )
print("Have fun with the other programs!")

#This will show up frequently, it's just to better seperate the different questions, anything can really be said here.
break_1 = input("Are you ready to continue? (You're forced to say yes)")

#Gets the number
chosen_number = int(input("Pick a number, any number *Said in an old school NY accent* "))

#decides whether odd, even, or zero
if chosen_number == 0:
  print ("Zero is too boring, but oh well.")
elif chosen_number % 2 == 0:
  print ("Guess what pal, it's even!")
elif chosen_number % 2 != 0:
  print ("You're an odd man by picking an odd number.")

#break
break_2 = input("Are you ready to continue? (Guess what it's gonna be yes anyways)")

#gets chosen day
chosen_day = int(input("Pick a day, any day (1 - 365) " ))

#finds out what month and subtracts previous days, this is a pretty lengthy and confusing process but it works by finding the month by using modified ranges and then subtracts all previous days so that it starts at day 1, leaving you with the remainder being the day of the date

#January
if chosen_day > 0 and chosen_day <= 31 :
  print("January:", chosen_day)

#Febuary
elif chosen_day > 31 and chosen_day <= 59 :
  print("Febuary:", chosen_day - 31)

#March
elif chosen_day > 59 and chosen_day <= 90 :
  print("March:", chosen_day - 59)

#April
elif chosen_day > 90 and chosen_day <= 120 :
  print("April:", chosen_day - 90)

#May
elif chosen_day > 120 and chosen_day <= 151 :
  print("May:", chosen_day - 120)

#June
elif chosen_day > 151 and chosen_day <= 181:
  print("June:", chosen_day - 151)

#July
elif chosen_day > 181 and chosen_day <= 212:
  print("July:", chosen_day - 181)

#August + my birthday
elif chosen_day == 234:
  print("You found my birthday of August:", chosen_day - 212)

elif chosen_day > 212 and chosen_day <= 243:
  print("August:", chosen_day - 212)

#September
elif chosen_day > 243 and chosen_day <= 273:
  print("September:", chosen_day - 243)

#October
elif chosen_day > 273 and chosen_day <= 304:
  print("October:", chosen_day - 273)

#November
elif chosen_day > 304 and chosen_day <= 334:
  print("November:", chosen_day - 304)

#December 
elif chosen_day > 334 and chosen_day <= 365:
  print("December:", chosen_day - 334)

else:
  print("I'm pretty sure you were supposed to type 1 - 365")

#break
break_3 = input("Ready to continue (I think you know the drill) ")

#its the same as my next one, but it will just have an input instead
rows = 5

#creates that many rows
for i in range(0, rows + 1):
  #creates that many colunmns
    for j in range(rows, 0 + i, -1):
        print(j, end=" ")
    print()

#same comments as before except I now ask for a number
row_input = int(input("Pick a max number"))

for i in range(0, row_input + 1):
    for j in range(row_input , 0 + i, -1):
        print(j, end=" ")
    print()

break_4 = input("BONUS QUESTION TIME")

#asks a number
day_num = int(input("Pick a number 1 - 365... again ", ))

#the remainder will tell you the number that is the order, minus sunday which = 0

if day_num % 7 == 0:
  print("Congrats! it's Sunday funday")
elif day_num % 7 == 6:
  print("Congrats! it's Saturday, enjoy you're weekend")
elif day_num % 7 == 5:
  print("Congrats! It's friday! I'm pretty sure there's a song about this")
elif day_num % 7 == 4:
  print("Eh I guess Thusday is ok")
elif day_num % 7 == 3:
  print("Wednesday, smack in the middle")
elif day_num % 7 == 2:
  print("Tuesday or Chooseday if you're weird")
elif day_num % 7 == 1:
  print("EVERYONE HATES MONDAYS")






