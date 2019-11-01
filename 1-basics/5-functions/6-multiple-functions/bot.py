def display_ladder(steps):
    for ladder in range(0, steps, 1):
        print("| |", "\n***")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()