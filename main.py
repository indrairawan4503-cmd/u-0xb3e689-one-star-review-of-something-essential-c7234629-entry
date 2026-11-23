import os

LINE = "Gravity has never once dropped my phone onto a bed. It waits until my hands are full, finds the one bare floor tile, screen first, and never misses. One star."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
