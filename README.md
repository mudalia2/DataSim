# DataSim

## Abstract

The following repository includes what I have primarily worked on my senior design project.  The portable multi-channel haptic feedback system aims to find a way to restore sensory feedback to an amputee through their prosthetic device. We achieve this using a system of tactile pressure sensors which can be embedded in a prosthetic device and a multi-channel electrical stimulator which will non-invasively provide stimulation across surface electrodes. The pressure sensors will modulate the sensation intensity as a function of the pressure measured on the fingertips
 
My part of the project deals with primarily the software side of the project. Therefore I will be working on the conversion of pressure sensor values to current values and also to implement a GUI to interact with the microcontroller circuit. The GUI will display the real time current output values and also sliders to set the default min/max values for each user.

## Introduction	
I have primarily worked on the software component of the project. This includes the Graphic User Interface and the conversion of pressure sensor values into current values in the microcontroller. However this repository will only include the GUI implementation due to a NDA.

The GUI is used to interact with the microcontroller in the sense that it polls current data in realtime to display it on the screen as well as send data to the DAC via USB to set the MIN/MAX current values determined for that particular user. The microcontroller software code interacts with the Pressure Sensor Module in so as to take in pressure sensor data. After parsing it passes these values into the DAC as voltage reference values. The DAC in turn interacts with constant current controller in the Stimulation Controller module. It passes analog voltage reference values into the constant current controller so that it produces current values. 
 
 
