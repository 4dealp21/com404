avoided_cables = 0

print("How many live cables must I avoid?")

cables_to_avoid = int(input())

while(avoided_cables < cables_to_avoid):

    avoided_cables = avoided_cables + 1
    print("Avoiding...", avoided_cables, "live cables avoided.")

print("All live cables have been avoided.")
