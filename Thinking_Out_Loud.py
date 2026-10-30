from rich import print 
from time import sleep

def printSong():
    Lyrics = [
        ("So baby now...", 0.08, 3.0),
        ("Take me into your loving arms", 0.08, 4.0),
        ("Kiss me under the light of a thousand stars", 0.08, 1.0),
        ("Oh darling", 0.05, 1.5),
        ("Place your head on my beating heart", 0.06, 2.0),
        ("I'm thinking out loud", 0.05, 1.5),
        ("That maybe we found love right where we are", 0.09, 5.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #FF69B4]{char}[/bold #FF69B4]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
            
printSong()

        