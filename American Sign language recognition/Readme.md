# NaoTherapy

This repository complements to the [NaoTherapy Android app](https://github.com/mmartinortiz/NaoTherapy-Android). Here you will find 3 different directories that contains behaviours created for Choreographe, the [Nao Robot](http://www.aldebaran.com/en) software suite.

## Emotions

This module is intended to help autistic children to recognize emotional body language. The module includes the ServerBox box, which receives messages from a [remote client](https://github.com/mmartinortiz/NaoTherapy-Android) and execute the appropriate emotion.

This behaviour includes all the emotions that the robot can interpret as well as different animation to congrat the child.

## Conversations

The aim of this exercise is help to autistic children to make appropriate questions. The exercise requires the robot, a set of cards with pictures and a therapist. The therapist controls the robot actions and speech. The robot has a card with a picture and the child has to figure out the picture. To discover the picture, the child can make any question he thinks appropriate.

The behaviour offers different movements allowing the user to make the robot more interactive. System behaviours can be called directly without need of a box and custom behaviours can be created inside this module.

## ServerBox

The **ServerBox** is a Choreographe box for the Nao Robot that allow you to send messages to the robot within the same network. With this messages, some basic aspects of the robot can be controlled remotely, for example, stop/start different behaviours installed in the robot

ServerBox should work with a NaoQi version >= 1.44. The message are formed as JSON objects sent to the server via socket. In [this](./ServerBox/doc/JSON.md) document you will find the message structure, tags and some examples

ServerBox opens a socket in the selected port. It receives JSON messages that decodes and interpret. The messages are received from the network where the robot is connected. Currently the messages are transmitted as plain text.

You can install the ServerBox Behaviour in the robot and set it as default behaviour. It does not require any robot resource (like motors), just the Unix socket. As basically it is a Python script, it can be easily adapted to your needs.

# How to use the files

The different projects (Emotions, Conversations and ServerBox) have to been open with the Choreographe Suite. You can find the suite on the [Aldebaran Website](http://www.aldebaran.com/en)

# Extending ServerBox

The box can be easily extended to accept other kind of messages or manipulate the robot behaviour according to different necessities. The ServerBox included in the Emotions behaviour has been modified, so take a look there to know the possibilities.

# License

NaoTherapy is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NaoTherapy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
