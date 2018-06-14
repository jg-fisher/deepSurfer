import keyboard
import cv2
import mss
import mss.tools
import numpy as np
import os
import sys


def _on_press(val, img):
    global img_count
    with open('actions.txt', 'a') as f:
        f.write('{}\n'.format(val))
    mss.tools.to_png(img.rgb, img.size, output=r'./images/frame-{0}_action-{1}.png'.format(img_count, val))
    img_count += 1

def _main():
        """
        Writes integer for respective action to text file.
        DOWN: 1
        UP: 2
        RIGHT: 3
        LEFT: 4
        """
        sct = mss.mss()
        mon = {
                'top': 60,
                'left': 0,
                'width': 420,
                'height': 720
        }

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

def _check_paths():
    """
    Checks for existence of data files. Option to overwrite.
    """
    if os.path.exists(r'./images'):
        overwrite = (input('Image folder exists. Do you want to overwrite? Y/N: ')).lower()
        if overwrite == 'y':
            pass
        elif overwrite == 'n':
            sys.exit()
    else:
        os.mkdir(r'./images')

    if os.path.exists(r'./actions.txt'):
        overwrite = (input('Actions.txt already exists. Do you want to overwrite? Y/N: ')).lower()
        if overwrite == 'y':
            pass
        elif overwrite == 'n':
            sys.exit()

if __name__ == '__main__':
    img_count = 0
    _check_paths()
    _main()
