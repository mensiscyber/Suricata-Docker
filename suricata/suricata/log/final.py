import smtplib
from email.message import EmailMessage
import sys
import re
from collections import deque
import imghdr
import yaml


with open("config.yml", 'r') as conyml:
    conf = yaml.load(conyml,Loader=yaml.FullLoader)

send_email = 'suricatatest01@gmail.com'
rev = 'terapat28@hotmail.com'
password_email = '??????????????'
files = ['Picture2.png','Picture3.png']
suricata_log = "fast.log"
search_strings = ["Priority: 2"]
smtp_sever = conf['smtp_server']
smtp_port = 465
subj = conf['subjectemail']

msg = EmailMessage()
msg['Subject'] = subj
msg['From'] = send_email
msg['To'] = rev
def send_mail(line_group):
    try:
        with smtplib.SMTP(smtp_sever, smtp_port) as smtp:
             smtp.login(send_email,password_email)
             smtp.send_message(msg)
    except:
            print("\nSMTP: NO CONNECTION\n")
           
with open(suricata_log) as log:
    line_group = deque(log, 1)
    for line in line_group:
        for string_item in search_strings:
            if string_item in line:
                   matches = re.search(r'^(?P<Date>.*?)-(?P<Time>)\s+\[.*?\]\s+\[.*?\]\s+(?P<alert>.*?)\s+\[.*?\]\s+\[(?P<classification>.*?)\]\s+\[(?P<Priority>.*?)\].*?(?P<scr_ip>\d+(?:\.\d+)*):(?P<scr_port>\d+)\s+->\s+(?P<Dess_ip>\d+(?:\.\d+)*):(?P<Dess_port>\d+).*$', line)
           
                   
                   h1 = (f'Date - {matches.group(1)}\n')
                   h2 = (f'Time - {matches.group(2)}\n')
                   h3 = (f'Alert - {matches.group(3)}\n')
                   h4 = (f'{matches.group(4)}\n')
                   h5 = (f'{matches.group(5)}\n')
                   h6 = (f'Source IP - {matches.group(6)}\n')
                   h7 = (f'Source Port - {matches.group(7)}\n')
                   h8 = (f'Destination IP - {matches.group(8)}\n')
                   h9 = (f'Destination Port - {matches.group(9)}\n')
                   msg.set_content('''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="https://fonts.googleapis.com/css?family=Muli:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i&amp;subset=latin-ext,vietnamese" rel="stylesheet">
</head>
<body>

<table  align="center" style="margin: 0px auto;cellpadding="0" cellspacing="0" border="0"  width="500">
<tr>
<td  colspan="2" style="background-color: #f1b514;   padding-top: 10px;padding-bottom: 0px;padding-left: 10px;padding-right: 30px;"><img src="Picture3.png" style="height: 100px;width:190px">
</td>
</tr>
<tr>
<td colspan="2" style="padding: 10px; background-color: #ededed; font-family: Impact New;font-size: 13pt; font-weight: bold">
    <center><img src="Picture2.png" style="height: 100px;width:190px"></center>
    <center><h1>Alert Rule</h1></center>
    <h3>{h1}<br/>
        {h2}<br/>
        {h3}<br/>
        {h4}<br/>
        {h5}<br/>
        {h6}<br/>
        {h7}<br/>
        {h8}<br/>
        {h9}<br/></h3>
<br/>
</td>
</tr>
<tr>
<td  colspan="2" style="background-color: #f1b514;   padding-top: 10px;padding-bottom: 10px;padding-left: 10px;padding-right: 40px;font-family: Times New RomanNew;font-size: 13pt; font-weight: bold">
<center>@Alert By Security Team</center>
<br/>
</td>
</td>
</tr>
</table>
</body>
</html>
'''.format(**locals()),subtype='html')
                   for file in files:
                     with open(file, 'rb') as f:
                        image_data = f.read()
                        image_type = imghdr.what(f.name)
                        image_name = f.name
                        msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name) 
                   send_mail(line_group)
                   sys.exit(0)