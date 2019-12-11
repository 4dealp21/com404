print("How many zones must I cross?")
number_zones = int(input())

print("Crossing zones...")

for zones in range(number_zones, 0, -1):
    print("…crossed zone", zones)

print("Crossed all zones.  Jumanji!")

