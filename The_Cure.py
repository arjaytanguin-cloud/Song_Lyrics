from rich import print
from time import sleep

def printSong():
    lyrics = [
        ("Why can't you come stitch me up?", 0.06, 0.5),
        ("Why can't it ever be enough?", 0.06, 1.0),
        ("Why can't you come stitch me up?", 0.08, 1.0),
        ("Why can't it ever be enough?", 0.08, 1.0),
        ("🎶...🎶...🎶", 0.09, 5.0),
        ("It's not enough", 0.08, 4.0),
        ("All because my head is full of poison", 0.08, 0.5),
        ("And my heart is full of doubt", 0.08, 1.0),
        ("I got toxins in my bloodstream", 0.06, 0.5),
        ("You tried so hard to suck out", 0.08, 8.0),

        
    ]

    for line, typing_speed, line_delay in lyrics:
        for char in line:
            print(f"[#000080]{char}[/#000080]", end="", flush=True)
            sleep(typing_speed)

        print()
        sleep(line_delay)

printSong()