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

# Képernyő felbontásának lekérdezése
screen_width, screen_height = 1920, 1080  # Példa érték

# Mappa elérési útvonala, ahol a képek találhatók
folder_path = os.path.join(os.getcwd(), 'work_images')

# Mappa elérési útvonala, ahol a számított képek lesznek
output_folder = os.path.join(os.getcwd(), 'computed_images')
# Mappa létrehozása az eredményeknek
current_date_time = datetime.now().strftime('%Y%m%d_%H%M%S')
output_folder_path = os.path.join(output_folder, current_date_time)
os.makedirs(output_folder_path)

# Arckereső szűrők
cascades_paths = [
    'haarcascade_frontalface_alt.xml',
    'haarcascade_frontalface_alt2.xml',
    'haarcascade_frontalface_alt_tree.xml',
    'haarcascade_frontalface_default.xml',
    'haarcascade_eye_tree_eyeglasses.xml',
    'haarcascade_profileface.xml',
    'haarcascade_fullbody.xml',
    'haarcascade_upperbody.xml',
]

# Színek definiálása
colors = [
    (255, 0, 0),    # Piros
    (0, 255, 0),    # Zöld
    (0, 0, 255),    # Kék
    (255, 255, 0),  # Sárga
    (255, 0, 255),  # Lila
    (0, 255, 255),  # Cián
    (128, 0, 0),    # Sötét piros
    (0, 128, 0),    # Sötét zöld
    (0, 0, 128),    # Sötét kék
    (128, 128, 0)   # Sötét sárga
]

# Minden kép feldolgozása
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # Kép betöltése
        img_path = os.path.join(folder_path, filename)
        print(img_path)
        img = cv2.imread(img_path)


        # Kép átalakítása szürkeárnyalatosra
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Minden szűrő alkalmazása
        for idx, cascade_path in enumerate(cascades_paths):
            # CascadeClassifier létrehozása
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)


            # Arcok detektálása a képen
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Felismert arcok keretezése a képen
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), colors[idx % len(colors)], 2)

        # Eredmény kép mentése
        output_file_path = os.path.join(output_folder_path, filename)
        cv2.imwrite(output_file_path, img)


        # Kép méretarányának meghatározása
        #ratio = min(screen_width / img.shape[1], screen_height / img.shape[0])
        # Kép átméretezése
        #resized_img = cv2.resize(img, (int(img.shape[1] * ratio), int(img.shape[0] * ratio)))

        # Eredmények megjelenítése
        #cv2.imshow('Detected Faces', resized_img)
        #cv2.imshow('Detected Faces', img)
        #cv2.waitKey(1000)  # Várunk egy másodpercet az eredmény megjelenítésére

cv2.destroyAllWindows()
