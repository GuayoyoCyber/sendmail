import base64
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

# Declare Variables
fromaddr = os.environ['FROM_ADDR']
toaddr = os.environ['TO_ADDR']
subject = os.environ['MAIL_SJT']
body = os.environ['MAIL_BODY']
filePath = os.environ['FILE_PATH']
atchType = os.environ['ATCH_TYPE']
atchName = os.environ['ATCH_NAME']
atchId = os.environ['ATCH_ID']
sendgridApiKey= os.environ['SENDGRID_API_KEY']

message = Mail(
    from_email=fromaddr,
    to_emails=toaddr,
    subject=subject,
    html_content=body)
    
with open(filePath, 'rb') as f:
    data = f.read()
    f.close()

encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType(atchType)
attachment.file_name = FileName(atchName)
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId(atchId)
message.attachment = attachment

try:
    sendgrid_client = SendGridAPIClient(sendgridApiKey)
    response = sendgrid_client.send(message)
    print('Mail sent Succesfully')
    print('Response: '+response.status_code)
    print('Response body: '+response.body)
    print('Response Headers: '+response.headers)
except Exception as e:
    print('Error while sending Email, see exception below: ')
    print(e.message)
