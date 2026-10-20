from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("Well now that you've got your gun", 0.08, 1.0), 
        ("It's much harder now police have come", 0.08, 1.0), 
        ("Now I'll shoot him that's what you ask", 0.08, 1.0), 
        ("But if You just take off your mask", 0.08, 1.0), 
        ("You'll find out, everything's gone now", 0.08, 1.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[#808080]{char}[/#808080]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
            