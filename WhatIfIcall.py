from rich import print
from time import sleep

def printSong():
    lyrics = [
        ("I miss you", 0.07, 1.0),

        ("You know it's true", 0.07, 1.0),
        ("Yeah i miss you", 0.07, 1.0),
        ("you know it's true", 0.07, 1.0),

        ("So what if I call?", 0.07, 1.0),
        ("And you pickup the phone", 0.07, 1.0),
        ("And I use this holiday to make my way to your ghost", 0.07, 1.0),
        ("What if you're lonely?", 0.07, 1.0),
        ("And you know I am too?", 0.07, 1.0),
        ("And I get the chance to say", 0.07, 1.0),
        ("I wish I didn't but I miss you.", 0.07, 1.0),
        ("I miss you", 0.07, 1.0)
    ]

    for line, typing_speed, line_delay in lyrics:
        for char in line:
                print(f"[#000080]{char}[/#000080]", end="", flush=True)
                sleep(typing_speed)

        print()
        sleep(line_delay)

printSong()