import pandas as pd
import cv2
import smtplib
email=[]
#you can also import file containing  mail ids.
for i in range(1805000,1806000):#i want to send mails to mail id 1805092@kiit.ac.in to 1805999@kiit.ac.in
    j=str(i)
    email.append(j+"@kiit.ac.in")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_mail_id@gmail.com","your_password")
msg = "One day left for the orientation!!! Grab your opportunity to get glimpses of the courses and exciting projects that we will be conducting in the upcoming weeks...Do register in the link https://forms.gle/m4aY8PHbmcrPi5R3A before it gets housefull"
subject = "KIIT ROBOTICS SOCIETY"
body="subject:{}\n\n{}".format(subject,msg)
for x in email:
    server.sendmail("your_mail_id@gmail.com",x,body)
    print(x+"  Done")
server.quit()
