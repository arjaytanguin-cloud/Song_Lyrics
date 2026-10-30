from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("Pull me oh so close", 0.08, 1.00),
        ("Cause you never know", 0.08, 1.00),
        ("Just how long our lives can be", 0.08, 3.00),
        ("If you've been waiting for falling inlove", 0.08, 1.00),
        ("Babe you don't have to wait on me", 0.08, 1.00),
        ("Cause I've been waiting for heaven above", 0.08, 1.00),
        ("But an angel ain't what I need", 0.08, 5.00),
        
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
            for char in line:
                print(f"[bold #FF0000]{char}[/bold #FF0000]", end="", flush=True)
                sleep(typing_speed)
                
            print()
            sleep(line_delay)
            
printSong()