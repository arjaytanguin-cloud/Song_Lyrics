from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("And I've been seeing somebody", 0.08, 1.0), 
        ("But I've not found a way to tell you", 0.08, 1.0), 
        ("That I'm seeing somebody", 0.08, 1.0), 
        ("There's not a nice way for me to say that", 0.08, 1.0), 
        ("I've been seeing somebody", 0.08, 1.0), 
        ("You know I want you to be happy", 0.08, 1.0), 
        ("Since I'm seeing somebody", 0.08, 1.0), 
        ("And then maybe we can get on with it", 0.08, 1.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[#800000]{char}[/#800000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()