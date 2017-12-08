import cv2, os
import numpy as np
from PIL import Image

print(help(cv2.face))

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')

        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])

        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids

faces, ids = getImagesAndLabels('Training Faces')
recognizer.train(faces, np.array(ids))
recognizer.write('trainer.yml')