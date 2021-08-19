# Human-robot-sign-language-Tutor

This application demonstrate how the NAO robot can recognize ASL(American alphabet signs) using deep learning algorithms and machin learning. It comes with a pre-trained deep learning model that allows NAO to recognize 26  different American alphabet signs with its camera.


To implant our model we borrowed SoftBank Object recognition on NAO with Deep Learning application screepts and sourse code ,manipuleted code to create our own application.
The original application and trained the model on google colab IDE based on Tiny YOLOv4.

We traind our own deep learning model with ASL image dataset and uploaded the model to be used in this application.

## About the Project
 The project is aimed to utilize humanoid robots for sign language tutoring. Humanoid robot Nao V6 as a subject is proposed to design the sign language tutoring program for sign language learner especially children. This will be accomplished by designing an interaction learning focused on visual communication, turn-taking, imitation, and developing specifically for robots and learner (children) to take part and give children a splendid chance to learn and quickly apply new signs. 


This project designed in two steps, first step is sign language recognition were we create a sign detector, which detects the alphabets that can very easily be extended to cover a vast multitude of other signs and hand gestures including the numbers from 1 to 10.
This is divided into 3 parts:
1.	Creating the dataset
2.	Training a CNN on the captured dataset
3.	Predicting the data

## The requirements software & libraries for the sign language project are:

*	Python (3.7.4)

* IDE (Jupyter)

* Numpy (version 1.16.5)

* cv2 (openCV) (version 3.4.2)

* Keras (version 2.3.1)

*	Tensorflow (as keras uses tensorflow in backend and for image preprocessing) (version 2.0.0)
*	1. Hardware & software compatibility
*	For American gesutre recognition Nao Application.
*	choregraphe-version-2.8.6.23-win64 
This app is compatible with NAO V6, and Naoqi 2.8.6


## Some key architectural insights into the project

I used opencv to take a frame running average of the background and then utilised that running average to detect the hand that needed to be inserted after the background was adequately recognised.
I found this great article on foreground masking by [(https://github.com/Gogul09)], and I pretty much utilised his code for backgrounds removal with a few tweaks to fit my needs. He's written an excellent article on the subject, which you can read here [(https://gogul09.github.io/software/hand-gesture-recognition-p1)].

### The Deep Convolution Neural Network

The model achieves an accuracy of **100%** on the validation dataset.

The ratio of training set to validation set is **1000 : 100**.

## How to run the RealTime prediction
It needs to be run with model_edged.h5 the SignLanguageRrecogniser.py i

![Final view of the program interface](https://github.com/PARASTOOP/Human-robot-sign-language-Tutor/blob/main/project%20screenshot/full%20screen%20GU%20gesture%20recognition.PNG)


Well now it's time for some demo.

![demo of the Robot syestem](https://youtu.be/jrCVKKwnMdw)
Watch "Dewey The Humanoid Robot  designed to be a Sign Language tutor." on YouTube
(https://youtu.be/Y_03hPUITBY)
