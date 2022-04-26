# sendmail

Automated task to Send Email with Sendgrid in Python Language

## Usage

Use Python3 to execute script
Linux: sudo apt install python3.8

# Create email object
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)

message = Mail(
    from_email=fromaddr,
    to_emails=toaddr,
    subject=subject,
    html_content=body)

# Declare variables
fromaddr = os.environ['FROM_ADDR']
toaddr = os.environ['TO_ADDR']
subject = os.environ['MAIL_SJT']
body = os.environ['MAIL_BODY']
filePath = os.environ['FILE_PATH']
atchType = os.environ['ATCH_TYPE']
atchName = os.environ['ATCH_NAME']
atchId = os.environ['ATCH_ID']
sendgridApiKey= os.environ['SENDGRID_API_KEY']

# Send email
sendgrid_client = SendGridAPIClient(sendgridApiKey)
    response = sendgrid_client.send(message)