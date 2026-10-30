from rich import print
from time import sleep

def printSong():
    lyrics = [
        ("It makes me think about you", 0.06, 0.5),
        ("So I wear it when I sleep", 0.06, 1.0),
        ("I kept the broken zipper", 0.08, 1.0),
        ("And cigarette burns", 0.08, 1.0),
        ("Still rockin your", 0.08, 0.5),
        ("Hoodie baby even though it hurts", 0.08, 0.5),
        ("Still rocking your", 0.08, 1.0),
        ("If you want it back, if you want it back", 0.06, 0.5),
        ("I'm here waiting", 0.08, 1.0),
        ("Come take it back, come take it back", 0.08, 1.5),
        
    ]

    for line, typing_speed, line_delay in lyrics:
        for char in line:
            print(f"[#000080]{char}[/#000080]", end="", flush=True)
            sleep(typing_speed)

        print()
        sleep(line_delay)

printSong()

