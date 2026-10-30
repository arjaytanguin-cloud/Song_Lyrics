from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("Now, it's three in the mornin'", 0.09, 1.0),
        ("And I'm tryna' change your mind", 0.08, 0.5),
        ("Left you multiple missed calls", 0.08, 0.5),
        ("And to my message, you reply", 0.08, 0.5),
        ("Why'd you only call me when you're high?", 0.08, 1.0), 
        ("Hi, why'd you only call me when you're high?", 0.08, 1.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF8700]{char}[/bold #FF8700]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
