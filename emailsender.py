import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr =   '   '
to_addr   =   '   '

msg=MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['subject'] = 'Just To Check'
body = 'Hello Brother, Did You recieve Email'

msg.attach(MIMEText(body,'Plain'))

email = ''
password = ''

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(mail,password)

text = msg.as_string()
mail.sendmail(from_addr,to_addrs,text)
mail.quit()