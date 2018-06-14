import keyboard
import cv2
import mss
import mss.tools
import numpy as np
import os
import sys


def on_press(val, img):
    global img_count
    with open('actions.txt', 'a') as f:
        f.write('{}\n'.format(val))
    mss.tools.to_png(img.rgb, img.size, output=r'./images/{0}_{1}.png'.format(val, img_count))
    img_count += 1

def main():
        """
        Writes integer for respective action to text file.
        DOWN: 1
        UP: 2
        RIGHT: 3
        LEFT: 4
        """
        while True:
            # screengrab
            img = sct.grab(mon)
            cv2.imshow('FRAME', np.array(img))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            # keypress callbacks
            keyboard.on_press_key('down', lambda _: on_press('1', img), suppress=True)
            keyboard.on_press_key('up', lambda _: on_press('2', img), suppress=True)
            keyboard.on_press_key('right', lambda _: on_press('3', img), suppress=True)
            keyboard.on_press_key('left', lambda _: on_press('4', img), suppress=True)


if __name__ == '__main__':
    mon = {
            'top': 0,
            'left': 0,
            'width': 0,
            'height': 0
            }
    
    sct = mss.mss()
    img_count = 0

    if os.path.exists(r'./images'):
        overwrite = (input('Image folder exists. Do you want to overwrite? Y/N: ')).lower()
        if overwrite == 'y':
            pass
        elif overwrite == 'n':
            sys.exit()
    else:
        os.mkdir(r'./images')

    main()
