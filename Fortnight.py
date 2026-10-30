from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("I love you, it's ruining my life", 0.08, 2.0), 
        ("(I love you, it's ruining my life)", 0.08, 2.5), 
        ("I touched you for only a fortnight", 0.08, 2.5), 
        ("(I touched you) I touched you", 0.08, 2.0), 
        ("Thought of callin' ya, but you won't pick up", 0.08, 2.0), 
        ("'Nother fortnight lost in America", 0.08, 1.5), 
        ("Move to Florida, buy the car you want", 0.08, 2.0), 
        ("But it won't start up 'til it touch, touch, touch you", 0.08, 5.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #800000]{char}[/bold #800000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
