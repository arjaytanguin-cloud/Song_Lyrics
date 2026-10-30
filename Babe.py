from rich import print
from time import sleep

def printSong():
    Lyrics = [        
        ("This is the last time, I'll ever call you babe", 0.05, 1.0), 
        ("Since you admitted it", 0.09, 1.0),
        ("I keep picturing", 0.09, 1.0),
        ("Her lips on your neck", 0.09, 1.0),
        ("I can't unsee it", 0.09, 1.0),
        ("I hate that because of you", 0.09, 1.0),
        ("I can't love you, babe", 0.09, 5.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #800000]{char}[/bold #800000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
            
printSong()