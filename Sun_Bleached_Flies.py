from rich import print
from time import sleep

def printSong():

    Lyrics = [
      ("If it's meant to be then it will be", 0.09, 4.0),
      ("So I met him there and told him I believe", 0.09, 5.5),
      ("Singing if it's meant to be then it will be", 0.09, 4.0),
      ("I forgive it all as it comes back to me", 0.09, 9.0),

    ]

    for line, typing_speed, line_delay in Lyrics:
            for char in line:
                print(f"[#D7D700]{char}[/#D7D700]", end="", flush=True)
                sleep(typing_speed)

            print()
            sleep(line_delay)
         
printSong()
