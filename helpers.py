import os
from collections import deque

class Helpers:
    def __init__(self):
        pass

    def last_frame(self):
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
    
    def remove_mistakes(self):
    
        last_frame = self.last_frame()
    
        mistakes = 3
    
        for img in os.listdir('images'):
            for delete in range(mistakes):
                if img.endswith('.png') and str(last_frame - delete) in img:
                    os.remove(r'./images/{}'.format(img))
    
        last_frame = self.last_frame()
    
        return last_frame


if __name__ == '__main__':
    helper = Helpers()
    print('Total frames: {}'.format(helper.last_frame()))
    print('Total frames - mistakes: {}'.format(helper.remove_mistakes()))

