import cv2
import sys
import numpy as np
import keras
from keras.models import load_model


def nothing(x):
    pass


def get_class_label(val, dictionary):
    for key, value in dictionary.items():
        if value == val:
            return key


model = load_model('model_edged.h5')

alphabet = {chr(i+96).upper():i for i in range(1,27)}
alphabet['del'] = 27
alphabet['nothing'] = 28
alphabet['space'] = 29

video_capture = cv2.VideoCapture(0)
cv2.namedWindow('Model Image')

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.createTrackbar('lower_threshold', 'Model Image', 0, 255, nothing)
cv2.createTrackbar('upper_threshold', 'Model Image', 0, 255, nothing)
cv2.setTrackbarPos('lower_threshold', 'Model Image', 100)
cv2.setTrackbarPos('upper_threshold', 'Model Image', 0)

THRESHOLD = 0.85
N_FRAMES = 5

IMG_SIZE = 100
SENTENCE = ''
letter = ''
LETTERS = np.array([], dtype='object')

START = True

description_text_2 = "Press 'D' to erase the output. "
description_text_3 = "Press 'Q' to quit."

while True:
    blank_image = np.zeros((100,800,3), np.uint8) # black image for the output
    ret, frame = video_capture.read() # capture frame-by-frame
	

    HandSignFrameX0 = 0
    HandSignFrameY0 = 0
    HandSignFrameX1 = int(HandSignFrameX0 + 400)
    HandSignFrameY1 = int(HandSignFrameY0 + 400)

    hand = frame.copy()[HandSignFrameY0:HandSignFrameY1, HandSignFrameX0:HandSignFrameX1] # crop model image
    gray = cv2.cvtColor(hand, cv2.COLOR_BGR2GRAY) # convert to grayscale
    # Noise Reduction
    blured = cv2.GaussianBlur(gray, (5, 5), 0)
    blured = cv2.erode(blured, None, iterations=2)
    blured = cv2.dilate(blured, None, iterations=2)

    lower = cv2.getTrackbarPos('lower_threshold', 'Model Image')
    upper = cv2.getTrackbarPos('upper_threshold', 'Model Image')
    edged = cv2.Canny(blured,lower,upper)

    model_image = ~edged #Invert colors
    model_image = cv2.resize(
        model_image,
        dsize=(IMG_SIZE, IMG_SIZE),
        interpolation=cv2.INTER_CUBIC
    )
    model_image = np.array(model_image)
    model_image = model_image.astype('float32') / 255.0

    try:
        model_image = model_image.reshape(1, IMG_SIZE, IMG_SIZE, 1)
        predict = model.predict(model_image)
        for values in predict:
            if np.all(values < 0.5):
                letter = 'Cannot classify:('
            else:
                predict = np.argmax(predict, axis=1) + 1
                letter = get_class_label(predict, alphabet)
                LETTERS = np.append(LETTERS, letter)
    except:
        pass


    if START == True:
        if (np.mean(LETTERS[-N_FRAMES:] == letter) >= THRESHOLD) & (len(LETTERS) >= N_FRAMES):
            if letter == 'space':
                SENTENCE = SENTENCE[:-1] + ' ' + '_'
                LETTERS = np.array([], dtype='object')
            elif letter == 'del':
                SENTENCE = SENTENCE[:-2] + '_'
                LETTERS = np.array([], dtype='object')
            elif letter == 'nothing':
                pass
            else:
                SENTENCE = SENTENCE[:-1] + letter + '_'
                LETTERS = np.array([], dtype='object')


    if START == False:
        paused_text = 'Paused'
    else:
        paused_text = ''

    # TEXT INITIALIZATION
    # paaused text
    cv2.putText(
        img=frame,
        text=paused_text,
        org=(HandSignFrameX0+140,HandSignFrameY0+195),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        color=(0,0,255),
        fontScale=1
    )

    cv2.putText(
        img=frame,
        text=description_text_2,
        org=(10,455),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        color=(255,255,255),
        fontScale=1
    )

    cv2.putText(
        img=frame,
        text=description_text_3,
        org=(10,470),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        color=(255,255,255),
        fontScale=1
    )

    cv2.putText(
        img=frame,
        text='Place your hand here:',
        org=(HandSignFrameX0+30,HandSignFrameY1-10),
        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
        color=(255,255,255),
        fontScale=1
    )

    # current letter
    cv2.putText(
        img=frame,
        text=letter,
        org=(HandSignFrameX0+10,HandSignFrameY0+20),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        color=(255,255,255),
        fontScale=1
    )

    # final output
    cv2.putText(
        img=blank_image,
        text='Result: ' + SENTENCE,
        org=(10, 50),
        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
        thickness=1,
        color=(0,0,255),
        fontScale=1
    )

    cv2.rectangle(frame, (HandSignFrameX0, HandSignFrameY0), (HandSignFrameX1, HandSignFrameY1), (0x00, 0x00, 0xFF), 1)

    cv2.imshow('Main Image', frame)
    cv2.imshow('Model Image', edged)
    cv2.imshow('Output', blank_image)

    if cv2.waitKey(30) & 0xFF == ord('d'):
        SENTENCE = ''

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

text_file = open("Output.txt", "w")
text_file.write("%s" % SENTENCE)
text_file.close()
