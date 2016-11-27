import os, django, sys
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(os.path.dirname(os.path.dirname((os.getcwd()))) + "/fifteen_minute_difference")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
from fifteen_minute_difference import settings
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta
from fifteen_minute_app.models import *

def build_actionable_email(volunteer, activeEmail):
    msg = MIMEMultipart()
    msg['To'] = volunteer.emailAddr
    msg['From'] = "15 Minute Difference Team <hello@15minutedifference.com>"
    msg['Subject'] = activeEmail.subject
    msg.attach(MIMEText(activeEmail.htmlBody, 'html'))
    msg.attach(MIMEText(activeEmail.textBody, 'plain'))
    return msg

activeEmail = ActionableEmail.objects.filter(activeStart__lte=datetime.utcnow()).order_by('-activeStart')[0]
print activeEmail.subject

username = settings.SMTP_LOGIN
password = settings.SMTP_PASSWORD
host = settings.SMTP_HOST

try:
    mailServer = smtplib.SMTP(host, 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)

    for volunteer in Volunteer.objects.filter(nextReminderTime__lte=datetime.utcnow(), active=True):
        print "Sending to: ", volunteer.emailAddr
        volunteer.nextReminderTime = volunteer.nextReminderTime + timedelta(days=7)
        volunteer.save()
        msg = build_actionable_email(volunteer, activeEmail)
        mailServer.sendmail(settings.SMTP_FROM_ADDR, volunteer.emailAddr, msg.as_string())
        
except Exception as e:
    print(str(e))

finally:
    mailServer.close()
