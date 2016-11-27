import os, django, sys
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.getcwd()) + "/fifteen_minute_difference")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
from fifteen_minute_difference import settings
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
import make_ical
from datetime import datetime

def send_an_email(recipient, msg):
    username = settings.SMTP_LOGIN
    password = settings.SMTP_PASSWORD
    host = settings.SMTP_HOST

    try:
        mailServer = smtplib.SMTP(host, 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(settings.SMTP_FROM_ADDR, recipient, msg.as_string())
        mailServer.close()

    except Exception as e:
        print(str(e))

def send_welcome_email(recipient, firstDateTime=datetime.now()):
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = "15 Minute Difference Team <hello@15minutedifference.com>"
    msg['Subject'] = "Welcome to Fifteen Minute Difference!"
    message = "Hello there! It worked! Here is a calendar invite"
    msg.attach(MIMEText(message, 'plain'))
    
    iCalString = make_ical.make_15m_recurring_ical(firstDateTime)
    part = MIMEApplication(iCalString, Name="15mininvite")
    part["Content-Disposition"] = "attachment; filename=15min.ics"
    msg.attach(part)
    
    #print msg
    send_an_email(recipient, msg)
