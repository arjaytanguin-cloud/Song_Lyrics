from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("Crawling back to you ", 0.09, 1.5),
        ("Ever thought of calling when you've had a few", 0.08, 0.5),
        ("Cause I always do", 0.07, 1.0),
        ("Maybe I'm too", 0.09, 1.0),
        ("Busy being yours to fall for somebody new", 0.08, 1.5),
        ("Now I've though it through", 0.08, 1.0), 
        ("Crawiling Back to you", 0.08, 5.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF8700]{char}[/bold #FF8700]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()