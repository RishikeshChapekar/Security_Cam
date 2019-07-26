# Security_Cam
A security alert system kind of thing using a Raspberry Pi

Run as `python3 securityCam.py`

# Hardware
1. PiCam
2. Infrared Sensor connected to the Pi

# Concept

The way I used it was such that there was a IR sensor glued to the wall near the door frame which was connected to the Pi. The PiCam was positioned such that it covered as much of the room as possible. When the door opened, the IR sensor got triggered and the PiCam took a 10 second video and mailed it to me ( I created a gmail for my projects ).

You can choose any method you want to trigger the IR sensor

# Quick changes to make before starting the system.

Change the sender's email ID and password in the code to the ID you want to use as a sender. Same goes for the reciever
