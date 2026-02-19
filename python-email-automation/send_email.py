import smtplib
from email.mime.text import MIMEText
import getpass

def send_email():
    sender_address = 'adityashaw053@gmail.com'
    password = getpass.getpass()

    subject = 'itadi02-Machine Learning'
    body = """
            Hello Everyone!
            If you find this code or repo very useful
            for AI/ML then please follow me and don't
            forget to star the repo.

            Thank You !
            Aditya Kumar Shaw
        """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'adityashaw2573@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)

    server.sendmail(sender_address,
                    'adityashaw2573@gmail.com',
                    msg.as_string())

    server.quit()
    print("Email Sent Successfully!")

send_email()
