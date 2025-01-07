Email Sender Script
Overview
This Python script sends emails via an SMTP server using SSL. It is configured for Gmail but can be adapted for other providers.

Prerequisites
Python 3.x installed.
An email account supporting SMTP (e.g., Gmail).
For Gmail: Enable 2-Step Verification and create an App Password.
Usage
Configuration
Update the following variables in the script:

python
Copy code
smtp_server = "smtp.gmail.com"
smtp_port = 465
username = "your-email@gmail.com"
password = "your-app-password"
Email Content
Set the email details:

python
Copy code
msg['From'] = "sender@gmail.com"
msg['To'] = "receiver@gmail.com"
msg['Subject'] = "Test Email"
msg.set_payload("This is the email body.")
Running the Script
Replace placeholders with actual values.
Run the script:
bash
Copy code
python email_sender.py
Notes
Security: Avoid hardcoding credentials. Use environment variables or a .env file.
Dependencies: This script uses smtplib and email.mime.text, which are part of Python's standard library.
