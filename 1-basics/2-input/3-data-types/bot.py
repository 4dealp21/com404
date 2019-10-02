#Ask users (name/age/height/weight) and getting user's input
print("Hey, what's your name?")
name = str(input())

print("How old are you?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

#Calculate bmi
bmi = weight/height**2

#Display result
print(name, "you are", age, "years old and your bmi is", bmi)
