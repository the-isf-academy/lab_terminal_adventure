# This is a Python program. You should run it by typing "chest.py"

from urllib.request import urlretrieve
import threading
import datetime

def treasure():
    print("    something shining brightly from within, so bright you can't")
    print("    quite make out what it is.\n")

def monster1():
    print("    *rumble* *rumble* *rumble* \n")
    print("    You look around the reef, but nothing seems out of place.\n")

def monster2():
    print("    *rumble* *rumble* *rumble* \n")
    print("    A SEA MONSTER APPEARS FROM THE REEF! \n")
    print("    Without looking you grab the treasure from the chest.")
    print("    Quick, use mkdir to make a \"bag\" directory and mv to")
    print("    hide the treasure in the bag. ")
    print("    Then get back to the surface ASAP! The moster is coming! \n")
    print("    Don't forget to take your treasure bag with you!")
    now = datetime.datetime.now()
    with open(".timer", "w") as keyfile:
        keyfile.write(str(now))


secret = "318"

print("    You approach the chest and see that the lock is surprisingly free of rust.")
print("    In fact, the code dials turn smoothly. Try entering a code.")

guess = input("    > ")

if guess == secret:
    print("    The chest snaps open, releasing several huge air bubbles.")
    print("    You look into the chest and see...\n")
    urlretrieve("http://chrisproctor.net/images/fork.png", "treasure.png")
    timer1 = threading.Timer(1.0, treasure)
    timer2 = threading.Timer(3.0, monster1)
    timer3 = threading.Timer(5.0, monster2)
    timer1.start()
    timer2.start()
    timer3.start()
else:
    print("    nothing happens. Maybe next time.")
