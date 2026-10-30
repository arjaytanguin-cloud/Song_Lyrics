from rich import print
from time import sleep

def printSong():
    lyrics = [
        ("Have I ever told you?", 0.07, 1.0),
        ("I want you to the bone.", 0.07, 2.0),
        ("Have I ever called you?", 0.07, 1.0),
        ("When you are all alone?", 0.07, 3.0),
        ("And if I ever forget", 0.07, 1.0),
        ("To tell you how I feel", 0.07, 1.0),
        ("Listen to me now babe", 0.07, 1.0),
        ("I want you to the bone.", 0.07, 3.5)
    ]

    for line, typing_speed, line_delay in lyrics:
        for char in line:
                print(f"[#DDA0DD]{char}[/#DDA0DD]", end="", flush=True)
                sleep(typing_speed)

        print()
        sleep(line_delay)

printSong()