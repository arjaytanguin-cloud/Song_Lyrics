from rich import print 
from time import sleep 

def printSong(): 
    lyrics = [
         ("Come on baby", 0.08, 1.0), 
         ("This ain't the last time that I'll see your face", 0.08, 1.0), 
         ("Come on baby", 0.08, 1.0), 
         ("You said you'll find someone to take my place", 0.08, 1.0),
         ("I just don't believe that", 0.08, 1.0), 
         ("You have got it in you", 0.08, 1.0), 
         ("Cause we're just gonna keep 'doin it'", 0.08, 1.0),
         ("And every time I start to believe in anything you're saying", 0.08, 1.0),
         ("I'm reminded that I should be gettin over it", 0.08, 1.0)
    ] 

    for line, typing_speed, line_delay in lyrics: 
        for char in line: 
            print(f"[#000080]{char}[/#000080]", end="", flush=True)
            sleep(typing_speed) 

        print() 
        sleep(line_delay) 
        
printSong()
            
