
# This is a Python file. You can run it by typing "python ghost.py"

from pathlib import Path

if Path("key.txt").exists():
    print("    The ghost glances over at you. 'I hope you find some use for that key.'")
else:
    print("    You enter the cramped galley and notice a sad, lonely ghost wandering")
    print("    around. You always wondered if you would be afraid of ghosts, but")
    print("    somehow this feels completely normal. The ghost begins to speak.")
    print("")
    print("    'It has been a long while since I have seen anybody down here,' she says")
    print("    'I would like to give you a gift. Here's a key.'")

    with open("key.txt", "w") as keyfile:
        keyfile.write("    Even in the faint light of your lamp, the key has a golden gleam.")
