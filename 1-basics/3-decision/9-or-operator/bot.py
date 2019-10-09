#Getting user input
print("What type of adventure should I have?")
path = input()

#Evaluate which route to take based on user input
#Display the results
if ((path == "long") or (path == "safe")):
    print("Taking the safe route!")

elif ((path == "short") or (path == "scary")):
    print("Entering the dark forest!")

else:
    print("Not sure which route to take.")