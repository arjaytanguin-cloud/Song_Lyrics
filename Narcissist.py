from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("And I've been seeing somebody", 0.05, 0.5), 
        ("But I've not found a way to tell you", 0.05, 1.0), 
        ("That I'm seeing somebody", 0.03, 2.0), 
        ("There's not a nice way for me to say that", 0.03, 1.0), 
        ("I've been seeing somebody", 0.03, 2.0), 
        ("You know I want you to be happy", 0.05, 2.0), 
        ("Since I'm seeing somebody", 0.03, 1.0), 
        ("And then maybe we can get on with it", 0.05, 5.0), 
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #800000]{char}[/bold #800000]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
