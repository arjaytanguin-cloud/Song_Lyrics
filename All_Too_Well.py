from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("And did the twin flame bruise paint you blue?", 0.08, 1.0), 
        ("Just between us, did the love affair maim you too?", 0.08, 1.0), 
        ("'Cause in this city's barren cold", 0.08, 1.0), 
        ("I still remember the first fall of snow", 0.08, 2.0), 
        ("And how it glistened as it fell", 0.08, 2.0), 
        ("I remember it all too well...", 0.09, 3.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[#FF0000]{char}[/#FF0000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
