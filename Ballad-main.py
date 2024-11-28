# Imports go at the top
from microbit import *
import music

tune = [
    'E6:2',
    
    #3
    'F6:2','E6:2','F6:2','A6:2','G6:4','F6:2','E6:2',
    'C6:6','D6:2','D6:4','R:2','E6:2',
    'F6:2','E6:2','F6:2','A6:2','C7:4','A#6:2','A6:2',
    'G6:6','F6:2','A6:4','R:2','E6:2',

    #7
    'F6:2','E6:2','F6:2','A6:2','G6:4','F6:2','E6:2',
    'C6:6','D6:2','A5:4','C6:2','D6:2',
    'F6:2','E6:2','C6:2','D6:2','A5:4','C6:2','D6:2',
    'F6:2','E6:2','F6:2','A6:2','G6:6','R:2',

    #11
    'F6:2','E6:2','F6:2','A6:2','G6:4','F6:2','E6:2',
    'C6:6','D6:2','D6:4','R:2','E6:2',
    'F6:2','E6:2','F6:2','A6:2','C7:4','A#6:2','A6:2',
    'G6:6','F6:2','A6:4','R:2','E6:2',

    #15
    'F6:2','E6:2','F6:2','A6:2','G6:2','G6:2','F6:2','E6:2',
    'C6:6','D6:2','A5:4','C6:2','D6:2',
    'F6:2','E6:2','C6:2','D6:2','A5:4','C6:2','D6:2',
    'F6:2','E6:2','C6:2','D6:2','D6:4','R:2','D6:1','E6:1',
    
    #19
    'F6:4','R:2','F6:2','E6:2','F6:2','E6:2','D6:2',
    'C6:6','D6:2','D6:4','R:2','D6:1','E6:1',
    'F6:4','R:2','F6:2','E6:2','F6:2','G6:2','C6:4',
    'A6:10','R:2','D6:1','E6:1',
    
    #23
    'F6:4','R:2','F6:2','E6:2','F6:2','E6:2','D6:2',
    'C6:2','R:1','C6:2','R:1','D6:2','F6:4','R:2','F6:1','G6:1',
    'A6:2','A6:2','A6:2','A6:2','G6:2','F6:2','F6:2','G6:2',
    'A6:4','G6:2','R:2','A#6:4','A6:2','R:2',

    #27
    'F6:6','E6:2','E6:4','R:2','E6:2',
    'F6:2','E6:2','F6:2','A6:2','G6:6','R:2',
    'A6:6','F6:2','F6:4','A6:4',
    'C7:8','G6:4','R:4',

    #31
    'G#6:6','G6:2','G6:4','R:2','G6:2',
    'G#6:2','G6:2','G#6:2','C7:2','A#6:6','R:2',
    'C7:6','G#6:2','G#6:4','C7:4',
    'D#7:8','A#6:4','R:4',

    #35
    'B6:16','C#7:16','C#7:4','R:2','C7:2','C7:8',
    
    'R:16',
]

b = 0
direction = 1
volume = 255

#beating heart & volume control
@run_every(ms=120)
def draw():
    global b, direction, volume
    if pin_logo.is_touched():
        #control volume, left reduce right increase
        if button_a.is_pressed() and volume >= 0:
            volume -= 10
            volume = 0 if volume < 0 else volume

        if button_b.is_pressed() and volume <= 255:
            volume += 10
            volume = 255 if volume > 255 else volume

        # draw
        if b == 0:
            direction = 1
        elif b == 9:
            direction = -1
        b += direction
        for x in range(5):
            for y in range(5):
                if y == 0 and (x == 1 or x == 3):
                    display.set_pixel(x,y,b)
                elif y == 1 or y == 2:
                    display.set_pixel(x,y,b)
                elif y == 3 and (x >= 1 and x <= 3):
                    display.set_pixel(x,y,b)
                elif y == 4 and x == 2:
                    display.set_pixel(x,y,b)

            

@run_every(ms=50)
def check_touched():
    global b, volume
    set_volume(volume)
    if not pin_logo.is_touched():
        music.stop()
        display.clear()
        b = 0
        volume = 255

    

# Code in a 'while True:' loop repeats forever
while True:
    if pin_logo.is_touched():
        music.play(tune)
