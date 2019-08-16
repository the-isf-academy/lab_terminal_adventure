# This is a Python program. You can run it by typing "python desk.py"

from pathlib import Path

print("    The stateroom contains the ruins of an elegant office. Scraps of wallpaper")
print("    are peeling from the wall; there is an eel living in the chandelier.")
print("    There is a huge desk at the center of the room.")

if Path("../galley/key.txt").exists():
    print("    You try your key in the desk drawer, and it clicks open. There are")
    print("    many decaying pieces of paper. One has the numbers 318 written in")
    print("    a fine script.")
else:
    print("    You try to open the desk's drawer, but it is firmly locked.")
