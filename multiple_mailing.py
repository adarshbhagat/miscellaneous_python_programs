import pandas as pd
import cv2
import smtplib
email=[]
for i in range(1805035,1805045):
    j=str(i)
    email.append(j+"@kiit.ac.in")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("adarsh.nwd@gmail.com","transversal")
msg = "One day left for the orientation!!! Grab your opportunity to get glimpses of the courses and exciting projects that we will be conducting in the upcoming weeks...Do register in the link https://forms.gle/m4aY8PHbmcrPi5R3A before it gets housefull"
subject = "KIIT ROBOTICS SOCIETY"
body="subject:{}\n\n{}".format(subject,msg)
for x in email:
    server.sendmail("adarsh.nwd@gmail.com",x,body)
    print(x+"  Done")
server.quit()
