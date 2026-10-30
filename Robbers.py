from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("And when she's leaving your home", 0.08, 1.0), 
        ("She's begging you to stay, stay", 0.08, 1.0), 
        ("Stay, stay, stay", 0.08, 1.0), 
        
        ("I'll give you one more time", 0.08, 2.0), 
        ("We'll give you one more fight", 0.08, 2.0), 
        ("Said one more line", 0.08, 1.0), 
        ("There'll be a riot 'cause I know you", 0.08, 1.0), 
        
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold ##FF0000]{char}[/bold ##FF0000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
            