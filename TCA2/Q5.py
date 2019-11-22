health = 100

print("Your health is 100%. Escape is in progress...")

for something in range(0, 5, 1):
    print("…Oh dear, who is that?")
    response = input()

    if (response == "Smiler's Bot"):
        new_health = health - 20
        print("Time to jam out of here!")

    elif (response == "Hacker"):
        new_health = health + 20
        print("Yay! Better follow this one!")

    else :
        print("Phew, just another emoji!")

final_heath = something
print("Escaped! Health is", final_heath, "%")

    
