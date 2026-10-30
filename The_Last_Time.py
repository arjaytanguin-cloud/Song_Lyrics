from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("And right before your eyes", 0.09, 1.0),
        ("I'm breaking", 0.08, 0.5),
        ("No past, no reasons why", 0.08, 0.5),
        ("No past, no reasons why", 0.08, 0.5),
        
        ("This is the last time I'm asking you this", 0.08, 1.0), 
        ("Put my name at the top of your list", 0.08, 1.0), 
        ("This is the last time I'm asking you why", 0.05, 1.0), 
        ("You break my heart in the blink of an eye", 0.05, 1.0),
       
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF0000]{char}[/bold #FF0000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
