# Send email function is created 
# here and will be called by email_user.py.

from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="magicmagid26@googlemail.com"
    from_password="London75!"
    # Email from outlook.com will be sent to
    # email that user inputted
    to_email = email
    
    # Subject and message of email
    subject = "Height Data"
    # Height is in bold <strong> using HTML 
    message = "Hey there! Your height is <strong>%s</strong>. <br> Average height of all users is <strong>%s</strong> and that is calculated from <strong>%s</strong> users. <br> Thanks!" % (height, average_height, count)
    
    # Message variable is read as HTML 
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    # Goes to gmail server with port 587
    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    # Logs in to gmail account
    gmail.login(from_email, from_password)
    # Sends message
    gmail.send_message(msg)