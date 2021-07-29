# Human-robot-sign-language-Tutor

## About the Project
 The project is aimed to utilize humanoid robots for sign language tutoring. Humanoid robot Nao V6 as a subject is proposed to design the sign language tutoring program for sign language learner especially children. This will be accomplished by designing an interaction learning focused on visual communication, turn-taking, imitation, and developing specifically for robots and learner (children) to take part and give children a splendid chance to learn and quickly apply new signs. 


This project designed in two steps, first step is sign language recognition were we create a sign detector, which detects the alphabets that can very easily be extended to cover a vast multitude of other signs and hand gestures including the numbers from 1 to 10.
This is divided into 3 parts:
1.	Creating the dataset
2.	Training a CNN on the captured dataset
3.	Predicting the data

##The requirements software & libraries for the sign language project are:

*	Python (3.7.4)

* IDE (Jupyter)

* Numpy (version 1.16.5)

* cv2 (openCV) (version 3.4.2)

* Keras (version 2.3.1)

*	Tensorflow (as keras uses tensorflow in backend and for image preprocessing) (version 2.0.0)


## Some key architectural insights into the project

### Background Ellimination Algorithm

I have used opencv for taking a running average of the background for 30 frames and then use that running average to detect the hand that has to be introduced after the background has been properly recognized.

I had found a very useful article on foreground mask by [Gogul09](https://github.com/Gogul09) and i have pretty much used his code for background ellimination with a few changes in order to suit my cause.

He has written an awesome article on the problem and you can read it up [here](https://gogul09.github.io/software/hand-gesture-recognition-p1).

### The Deep Convolution Neural Network

The network contains **7** hidden convolution layers with **Relu** as the activation function and **1** Fully connected layer.

The network is trained across **50** iterations with a batch size of **64**.

I kind of saw that 50 iterations kind of trains the model well and there is no increase in validation accuracy along the lines so that should be enough.

The model achieves an accuracy of **96.6%** on the validation dataset.

The ratio of training set to validation set is **1000 : 100**.

## How to run the RealTime prediction




## Demo of how things look on the go

Well now it's time for some demo.

![Alt Text](https://github.com/)
