#Getting user's input
print("Please enter the first whole number.")
first_number = int(input())

print("Please enter the second whole number.")
second_number = int(input())

print("Please enter the third whole number.")
third_number = int(input())

#Creating a counter
evens = 0
odds = 0

#Check if the numbers are odd or even
if (first_number%2 == 0):
    evens = evens + 1

else:
    odds = odds + 1

if (second_number%2 == 0):
    evens = evens + 1

else:
    odds = odds + 1

if (third_number%2 == 0):
    evens = evens + 1

else:
    odds = odds + 1

#Display results
print("There were " + str(evens) + " even and "  + str(odds) + " odd numbers.")
