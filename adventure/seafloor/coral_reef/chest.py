# This is a Python program. You should run it by typing "chest.py"

from urllib.request import urlretrieve

secret = "318"

print("    You approach the chest and see that the lock is surprisingly free of rust.")
print("    In fact, the code dials turn smoothly. Try entering a code.")

guess = input("    > ")

if guess == secret:
    print("   The chest snaps open, releasing several huge air bubbles.")
    print("   You look into the chest and see...")
    urlretrieve("http://chrisproctor.net/images/fork.png", "treasure.png")
else:
    print("    nothing happens. Maybe next time.")
