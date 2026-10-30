from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("Oh Caroline", 0.08, 2.0),
        ("I wanna get it right this time", 0.08, 2.0),
        ("Cause your always on my mind", 0.08, 2.0),
        ("Oh Caroline", 0.08, 2.0)
    ]
    
    for line, typing_speed, line_delay in Lyrics:
            for char in line:
                print(f"[bold #800000]{char}[/bold #800000]", end="", flush=True)
                sleep(typing_speed)
                
            print()
            sleep(line_delay)
            
printSong()