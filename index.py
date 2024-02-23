#!/usr/bin/env python
'''
python 3.10
To install all required modules:
pip install -r requirements.txt
To update required modules:
pip install pipreqs
pipreqs . --force
'''

import os
import cv2
from datetime import datetime

folder_path = os.path.join(os.getcwd(), 'work_images')
output_folder = os.path.join(os.getcwd(), 'computed_images')

current_date_time = datetime.now().strftime('%Y%m%d_%H%M%S')
output_folder_path = os.path.join(output_folder, current_date_time)
os.makedirs(output_folder_path)

cascades_paths = [
    'haarcascade_frontalface_alt.xml',
    'haarcascade_frontalface_alt2.xml',
    'haarcascade_frontalface_alt_tree.xml',
    'haarcascade_frontalface_default.xml',
    'haarcascade_eye_tree_eyeglasses.xml',
    'haarcascade_profileface.xml',
    'haarcascade_fullbody.xml',
    'haarcascade_upperbody.xml',
    'HOGDescriptor_getDefaultPeopleDetector',
]

colors = [
    (255, 0, 0),    # Piros
    (0, 255, 0),    # Zöld
    (0, 0, 255),    # Kék
    (255, 255, 0),  # Sárga
    (255, 0, 255),  # Lila
    (0, 255, 255),  # Cián
    (128, 128, 0),   # Sötét sárga
    (128, 0, 0),    # Sötét piros
    (0, 128, 0),    # Sötét zöld
    (0, 0, 128),    # Sötét kék
]

for filename in os.listdir(folder_path):

    if filename.endswith(".jpg"):

        img_path = os.path.join(folder_path, filename)
        print(img_path)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for idx, methods in enumerate(cascades_paths):

            if ("haarcascade_" in methods):
                cascade = cv2.CascadeClassifier(cv2.data.haarcascades + methods)
                regions = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            elif ("HOGDescriptor_getDefaultPeopleDetector") in methods:
                hog = cv2.HOGDescriptor()
                hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                (regions, _) = hog.detectMultiScale(gray, winStride=(4, 4), padding=(4, 4), scale=1.05)

            for (x, y, w, h) in regions:
                cv2.rectangle(img, (x, y), (x+w, y+h), colors[idx % len(colors)], 3)

        output_file_path = os.path.join(output_folder_path, filename)
        cv2.imwrite(output_file_path, img)

cv2.destroyAllWindows()
