from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("You and I (Don't let go)", 0.08, 2.0),
        ("We're alive (Don't let go)", 0.08, 3.0),
        ("With nothing to do I could lay and just look in your eyes", 0.08, 7.0),
        ("Wait, (Don't let go)", 0.08, 3.0),
        ("And pretend (Don't let go)", 0.08, 3.0),
        ("Hold on and hope that we'll find our way back in the end", 0.08, 5.0),
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
           for char in line:
               print(f"[bold #800000]{char}[/bold #800000]", end="", flush=True)
               sleep(typing_speed)
               
           print()
           sleep(line_delay)               


printSong()