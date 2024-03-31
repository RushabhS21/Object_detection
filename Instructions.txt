1. Included all the required libraries like opencv to get the cvlib library which has multiple trained model
2. from that cvlib module used a object_detection model which help us to identify objects
3. now written logic to initialize window, model.
4. now created a list of objects which are shown by users
5. and with speech() method our script is able to say things loudly.

dependencies -
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

At the time of doing assignment, I'm aware of object detection and now I'm learning how anomaly detection works.
