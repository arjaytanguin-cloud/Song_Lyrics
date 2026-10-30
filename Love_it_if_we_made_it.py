from rich import print
from time import sleep

def printSong():
    Lyrics = [
        
        ("And poison me, daddy, I've got the Jones right through my bones", 0.08, 0.5),
        ("Write it on a piece of stone, a beach of drowning three-year-olds", 0.08, 0.5),
        ("Rest in peace Lil Peep, the poetry is in the streets", 0.08, 0.5),
        ("Jesus save us, modernity has failed us", 0.08, 0.5),
        ("And I'd love it if we made it", 0.08, 5.0),
        ("Yes I'd love it we made it", 0.08, 5.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
            for char in line:
                print(f"[bold #00005F]{char}[/bold #00005F]", end="", flush=True)
                sleep(typing_speed)
                
            print()
            sleep(line_delay)   
                
printSong()
    
    