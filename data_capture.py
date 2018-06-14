import keyboard
import cv2
import mss
import mss.tools
import numpy as np
import os
import sys
from helpers import Helpers

def _on_press(val, img):
    global img_count
    # creating labels when loading images for model
    #with open('actions.txt', 'a') as f:
    #    f.write('{}\n'.format(val))
    mss.tools.to_png(img.rgb, img.size, output=r'./images/frame-{0}_action-{1}.png'.format(img_count, val))
    print('Action {}.'.format(val))
    img_count += 1

def _main():
        """
        Writes integer for respective action to text file.
        NOTHING: 0
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
            keyboard.on_press_key('down', lambda _: _on_press('1', img), suppress=True)
            keyboard.on_press_key('up', lambda _: _on_press('2', img), suppress=True)
            keyboard.on_press_key('right', lambda _: _on_press('3', img), suppress=True)
            keyboard.on_press_key('left', lambda _: _on_press('4', img), suppress=True)
            keyboard.on_press_key('t', lambda _: _on_press('0', img), suppress=True)

def _check_paths():
    """
    Checks for existence of data files. Option to overwrite.
    """
    if os.path.exists(r'./images'):
        pass
    else:
        os.mkdir(r'./images')

    #if os.path.exists(r'./actions.txt'):
    #    overwrite = (input('Actions.txt already exists. Do you want to overwrite? Y/N: ')).lower()
    #    if overwrite == 'y':
    #        pass
    #    elif overwrite == 'n':
    #        sys.exit()

if __name__ == '__main__':
    helper = Helpers()
    _check_paths()

    # erase last few mistake frames
    if len(sys.argv) > 1 :
        if sys.argv[1] == '--delete':
            print('Total frames: {}'.format(helper.last_frame()))
            print('Total frames - mistakes: {}'.format(helper.remove_mistakes()))
            img_count = helper.last_frame()
            print('Starting frames at {}'.format(img_count))
    else:
        img_count = helper.last_frame()
        print('Total frames: {}'.format(img_count))
        
    _main()
