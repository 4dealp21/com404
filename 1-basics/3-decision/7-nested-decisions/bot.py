# Ask user what type of cover does the book have
print("What type of cover does the book have (soft/hard)?")
cover = input()

# Decide between soft and hard
if (cover == "soft"):

    #Get user input
    #Decide between perfect-bound or not
    print("Is the book perfect-bound (yes/not)?")
    bound = input()

    if (bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")

    else:
        print("Soft covers with coils or stitches are great for short books")

else:
    print("Books with hard covers can be more expensive!")