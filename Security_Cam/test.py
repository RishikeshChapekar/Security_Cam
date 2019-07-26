from picamera import PiCamera as pcam
import time
import datetime
import smtplib  
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders 
import sys
import os

x = str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace(".","_")

camera = pcam()
camera.rotation = 180
camera.start_preview()

camera.start_recording(x+".h264")
time.sleep(10)
camera.stop_recording()
camera.stop_preview()
os.system("MP4Box -add "+x+".h264 "+x+".mp4")
print("converted")
os.system("rm "+x+".h264")
smtpUser = 'sender@gmail.com'
smtpPass = 'sender_password'
toAdd = 'reciever@gmail.com'
fromAdd = smtpUser
def sendMail(to, subject, text, files=[]):
    
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = smtpUser
    msg['To'] = to
    msg['Date'] = x
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(smtpUser,smtpPass)
    server.sendmail(smtpUser, to, msg.as_string())

    print 'Done...email sent'

    server.quit()


sendMail( toAdd, "Request for image", "Good day  \n As per your request a video has been sent to you as clicked on "+x, [x+".mp4"] )


