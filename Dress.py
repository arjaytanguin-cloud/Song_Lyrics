from rich import print
from time import sleep

def printSong():
    Lyrics = [
        ("Flashback when you met me", 0.05, 0.5), 
        ("Your buzzcut and my hair bleached?", 0.05, 0.5), 
        ("Even in my worst times", 0.03, 1.0), 
        ("You could see the best in me", 0.03, 1.0),
        ("Flashback to my mistakes", 0.03, 1.0), 
        ("My rebounds, my earthquakes", 0.03, 1.0),
        ("Even in my worst lies", 0.05, 1.0), 
        ("You saw the truth in me", 0.09, 0.5),
        ("And I woke up just in time", 0.05, 0.5),
        ("Now I wake up by your side", 0.05, 1.5),
        ("My one and only, my lifeline", 0.05, 0.5),
        ("I woke up just in time", 0.06, 0.5),
        ("Now I wake up by your side", 0.05, 0.5),
        ("My hands shake, I can't explain this ah, ha, ha, ha", 0.09, 5.0),
        
        
    ]
    
    for line, typing_speed, line_delay in Lyrics:
        for char in line:
            print(f"[bold #8787AF]{char}[/bold #8787AF]", end="", flush=True)
            sleep(typing_speed)
            
        print()
        sleep(line_delay)
        
printSong()
