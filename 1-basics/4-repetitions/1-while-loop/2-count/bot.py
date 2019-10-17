interations = 0

print("How many live cables must I avoid?")

live_cables = int(input())

while(interations < live_cables):

    interations = interations + 1
    print("Avoiding...", interations, "live cables avoided.")

print("All live cables have been avoided.")
