from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("Missing everything you say", 0.09, 1.5),
        ("It's not important what you stand for", 0.08, 0.5),
        ("You're asking will he be the one", 0.07, 1.0),
        ("I'll be gone before you're done tonight", 0.09, 1.0),
        ("Waiting for another day", 0.08, 1.5),
        ("You're not getting what you paid for", 0.08, 1.0), 
        ("Trying to salvage what's undone and deny you got outrun tonight", 0.08, 5.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF8700]{char}[/bold #FF8700]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
