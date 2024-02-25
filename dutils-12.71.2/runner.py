import os

def cls():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)

session = 0

while True:
    session += 1
    cls()
    print(f"\n\n\nRunning dutils session {session}...\n\n\n")
    os.system("python ./main.py")
    continue

