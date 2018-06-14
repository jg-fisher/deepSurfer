from model import CRNN
import cv2
import os
from collections import deque
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import torch
from torch.utils.data import DataLoader

X = deque()
Y = deque()

for img in os.listdir('images'):
    if img.endswith('.png'):
        frame = cv2.imread(r'./images/{}'.format(img), cv2.IMREAD_GRAYSCALE)
        # check syntax on these two
        #img = cv2.Canny(img, (100, 200))
        #img = cv2.resize(img, (64, 64))
        X.append(frame)
        print('X', X)

        # correct label for frame
        action = [c for c in img]
        action = [x for i, x in enumerate(action) if action[i-1] is '-'][1]
        Y.append(action)
        print('Y', Y)

# input, hidden, ouput
#model = CRNN()

X, Y = shuffle(X, Y, random_state=0)








