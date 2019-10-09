print("Where should I look?")
first = input()

if (first == "in the bedroom"):
    print("Where in the bedroom should I look?")
    second = input()

    if (second == "under the bed"):
        print("Found some shoes but no battery")

elif (first == "in the bathroom"):
    print("Where in the bathroom should I look?")
    third = input()

    if (third == "in the bathtub"):
        print("Found a rubber duck but no battery")

elif (first == "in the lab"):
    print("Where in the lab should I look?")
    fourth = input()

    if (fourth == "on the table"):
        print("Yes! I found my battery!")

else:
    print("I do not know where that is but I will keep looking.")

