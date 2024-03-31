import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    lang = "en"
    output = gTTS(text=text, lang=lang, slow=False)

    output.save("D:\\Object detection\\sounds\\op.mp3")
    playsound("D:\\Object detection\\sounds\\op.mp3")

video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_img = draw_bbox(frame,bbox,label,conf)

    cv2.imshow("OBJD", output_img)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
            
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i = 0
new_sentence = []
for label in labels:
    if i==0:
        new_sentence.append(f"I found a {label}, and ")
    else:
        new_sentence.append(f"a {label} ")
    i += 1

speech(" ".join(new_sentence))