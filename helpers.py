import os
from collections import deque

def last_frame():
    """
    Begins new frames at last frame
    """
    images = []
    
    for img in os.listdir('images'):
        if img.endswith('.png'):
            num = img.split('-')[1]
            num = num.split('_')
            images.append(num[0])
    
    max = 0
    for i in images:
        if int(i) > int(max):
            max = i
    
    return int(max) + 1


if __name__ == '__main__':
    print('Total frames: {}'.format(last_frame()))
