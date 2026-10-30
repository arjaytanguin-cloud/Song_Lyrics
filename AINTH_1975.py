from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("Cause I don't need music, in my ears", 0.08, 3.0),
        ("I dont need the crowds and the cheers", 0.08, 2.0),
        ("Oh just tell me you love me", 0.08, 1.0),
        ("Cause that's all that I need to hear", 0.08, 6.0),
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[#000080]{char}[/#000080]", end="", flush=True)
            sleep(typing_speed)

        print()
        sleep(line_delay)
        
printSong()
