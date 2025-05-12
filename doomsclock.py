import time
import sys
import random

p = input("Enter planet: ")
s = input("Enter your species: ")
n = input("Enter your name: ")
inp = 2025 - (int(input("Enter your birth year: ")))
d = random.randint(0, inp * 662256000)

print("\n\nLoading DOOMSCLOCK...")

time.sleep(6)

print("\nMortal Identification-->\n")
print(f"Habitat: {p}")
print(f"Species: {s}")
print(f"Local identity (referred to as 'name'): {n}")
print(f"Age: {inp}")
for i in range(d,0,-1):
    print(f"Time left: {i} seconds")
    time.sleep(1)

    if not i==1:
        sys.stdout.write("\33[F\33[K")

    else:
        print("Time's up. You lived long enough!!!")