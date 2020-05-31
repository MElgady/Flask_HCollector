# Send email function is created
# here and will be called by email_user.py.

from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    # Comment added: 11/05/2020
    # New email and password used for this application
    # Note: This change has to be sent to Heroku server!
    from_email = "heightcollectorapp9@gmail.com"
    from_password = "Height75"
    # Email from gmail.com will be sent to
    # email that user inputted
    to_email = email

    # Subject and message of email
    subject = "Height Data"
    # Height is in bold <strong> using HTML
    message = "Hey there! Your height is <strong>%scm</strong>. <br> Average height of all users is <strong>%scm</strong> and that is calculated from <strong>%s</strong> users. <br> Thanks!" % (
        height, average_height, count)

    # Message variable is read as HTML
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # Goes to gmail server with port 587
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    # Logs in to gmail account
    gmail.login(from_email, from_password)
    # Sends message
    gmail.send_message(msg)
