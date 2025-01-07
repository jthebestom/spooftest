import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
smtp_port = 465
username = "your-email@gmail.com"
password = "your-app-password"


msg = MIMEText("This email appears to come from someone else!")
msg['From'] = "fake.sender@gmail.com"
msg['To'] = "receiver"
msg['Subject'] = "spoofed "
msg['Reply-To'] = "fake.sender@gmail.com"


try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(username, password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
