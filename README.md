# Cafeteria-Occupancy-with-Samsung-Artik
Identifying number of seats/people occupied in cafeteria without using sensor.

This setup revolves around an idea to provide better office experience. Usually, during peak hours in lunchtime, it's hard to find any seat and that too after re-scheduling a meeting. Employees can get benefit by just accessing the cafeteria occupancy data and can have their lunch without ending or rescheduling the meeting. 
Here, I have used IPcamera to take picture of a certain area in the cafeteria with 5 mins interval. The captured image is then processed using the deep learning python code, which identifies how many people present in an area and posts the count value to any cloud service. I have used Samsung Artik Cloud to visualize the data.

## Steps to follow:
1.	Setting up the Gateway to receive and process the image from IPcamera. I have used Raspberry Pi setup: https://github.com/niladri30/IPCamera-Raspberry-Pi-setup 
2.	Node-red Flow to actuate the IPcamera and take a snapshot every 5 mins interval. The image is then processed using the python script.
3.	Create a Samsung Artik cloud account(https://my.artik.cloud/).

## Block Diagram
![alt text](https://github.com/niladri30/Cafeteria-Occupancy-with-Samsung-Artik/blob/master/images/ipcam.PNG)

Deploy the Node-Red flow to trigger the complete process. 

![alt text](https://github.com/niladri30/Cafeteria-Occupancy-with-Samsung-Artik/blob/master/images/node-red.PNG)

To display on Samsung Artik Cloud, add device by selecting:

![alt text](https://github.com/niladri30/Cafeteria-Occupancy-with-Samsung-Artik/blob/master/images/artik.png)

Go to Charts and view the incoming data:

![alt text](https://github.com/niladri30/Cafeteria-Occupancy-with-Samsung-Artik/blob/master/images/Capture.PNG)

## File used:
1.  face1.py  :  This is used to capture the image from the IPcamera and save it as face1.jpg  
2.  FirstDetection.py : This is used to run AI on the capture image.

For person detection, I have taken reference from https://github.com/OlafenwaMoses/ImageAI
