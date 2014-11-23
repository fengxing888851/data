#! /usr/bin/python

import smtplib
import xlrd 

#data = xlrd.open_workbook(r'/home/mgl/Downloads/mid-term examination.xlsx')
#table = data.sheet_by_name(u'Sheet1')

sender = 'fdumgl@163.com'
#receivers = table.col_values(0)
#scores = table.col_values(2)
#person = map(None, receivers, scores)
#print person
smtpObj = smtplib.SMTP()
smtpObj.connect('smtp.163.com')
#smtpObj.helo()
smtpObj.login('fdumgl@163.com', '20100212a')
#smtpObj.helo()

person = [('13110220047','100'),('13210370002','2')]
for (user, score) in person:
   message = """From: Gongli Ma <fdumgl@163.com>
   To: %s <%s@fudan.edu.cn>\n\n
   Subject: Mid-term examination\n\n

   Student ID: %s 
   \n\s\s Score: %s \n
   """%(user, user, user, score)
   con = '\n\n\s\s contratulations'
   try:
      if int(score) >= 90:
         smtpObj.sendmail(sender, (user+'@fudan.edu.cn'), (message+con))         
      else:
         smtpObj.sendmail(sender, (user+'@fudan.edu.cn'), message)         
      print "Successfully sent email"
   except smtplib.SMTPException:
      print "Error: unable to send email"
      print user
smtpObj.quit()
