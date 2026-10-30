from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("Distract my brain from the terrible news", 0.08, 1.0),
        ("It's not living if it's not with you", 0.08, 0.8),
        ("Oh and johnny got a job in the bank i think", 0.08, 0.5),
        ("Danny spent the time trying to pack in the drinks for me", 0.06, 0.5),
        ("I feel sick and I know that i'll lose but", 0.08, 1.0),
        ("It's not living if it's not with you", 0.07, 5.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF00FF]{char}[/bold #FF00FF]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)   
            
printSong()
