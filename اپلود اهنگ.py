from pygame import mixer
import time
while True:
    mixer.init()
    mixer.music.load("11.mp3")
    mixer.music.play(start=9)
    time.sleep(40)

