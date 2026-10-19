from rich import print
from time import sleep

def printSong():
    lyrics = [
        ("I'm still rockin' your hoodie", 0.08, 1.0),
        ("And chewin' on the strings", 0.08, 2.0),
        ("It makes me think about you", 0.08, 1.0),
        ("So I wear it when I sleep", 0.08, 3.0),
        ("I kept the broken Zipper", 0.08, 1.0),
        ("And cigarette burns", 0.08, 1.0),
        ("Still rockin your", 0.08, 1.0),
        ("Hoodie baby even though it hurts", 0.08, 3.5)
    ]

    for line, typing_speed, line_delay in lyrics:
        for char in line:
            print(f"[#000080]{char}[/#000080]", end="", flush=True)
            sleep(typing_speed)

        print()
        sleep(line_delay)

printSong()

