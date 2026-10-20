from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("I'm caught on your coat again", 0.08, 1.0), 
        ("You said 'Oh no it's fine'", 0.08, 1.0), 
        ("I read between the lines and touched your leg again", 0.08, 1.0), 
        ("I'll take it one day at a time", 0.08, 1.0), 
        ("Soon you will be mine, oh, but i want you now", 0.08, 1.0), 
        ("When the smoke get's in your eyes", 0.08, 1.0),
        ("You look so alive", 0.08, 1.0),
        ("Do you fancy sitting down with me?", 0.08, 1.0),
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[#808080]{char}[/#808080]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()