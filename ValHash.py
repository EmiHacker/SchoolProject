import hashlib
import os
import re
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class HASH:
    def generarHash(h):
        digest=h.hexdigest()
        return digest
    
ruta = ''#Change this rute
os.chdir(ruta)
for root, dirs, files in os.walk(".", topdown=False):
    valores=[]
    for name in files:
        if re.findall('encriptado.txt$',name):
            archivos=open(name,'r')
            texto=archivos.readlines()
            archivos.close
            texto=(str(texto))
            bdatos = bytes(texto, 'utf-8')
            h=hashlib.new('sha256',bdatos)
            hash1=HASH.generarHash(h)
            print(hash1)
            valores.append(hash1)

    with open('ValoresHash.txt','w') as Hash:
        valores=(str(valores))
        Hash.write('ValHash256:\n')
        Hash.write(valores)
        Hash.close()

smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('user','pwd') #user: email, pwd: password

def send_test_mail(body):
    sender_email = #user
    receiver_email = #another_user
    msg = MIMEMultipart()
    msg['Subject'] = "Estos son los valores hash: "
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)
    try:
      with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('user','pwd')
        smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
      print(e)

if __name__ == "__main__":
    f = open("ValoresHash.txt", "r")
    mensaje = f.read()
    send_test_mail(mensaje)
