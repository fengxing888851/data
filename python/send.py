# --* utf-8 *--
import smtplib
import xlrd
from email.mime.text import MIMEText
import datetime
import time

def sendmail(name='test',address='13210370002',score="0"):
    template = '''
    <body>
         <h>Dear student <b> %s </b> : </h> <p/> <p/>
	 &nbsp; &nbsp; Your score is <b> %s </b> . <p/>
         &nbsp; &nbsp; Wish you have a better score at final exam! <p/> <p/> <p/>
         %s
    </body>
    ''' %(name,score,datetime.date.today())
    server = smtplib.SMTP()
    server.connect('mail.fudan.edu.cn')
    server.ehlo()
    server.login('xiaojiezhang12@fudan.edu.cn','120017')
    server.ehlo()
    msg = MIMEText(template,_subtype='html',_charset='utf-8')
    msg['Subject'] = 'Physical chemistry mid-term score'
    msg['To'] = address+'@fudan.edu.cn'
    server.sendmail('xiaojiezhang12@fudan.edu.cn',address+'@fudan.edu.cn',msg.as_string())
    server.close()

if __name__ == "__main__":
#    sendmail()
    data = xlrd.open_workbook(r'/home/mgl/Downloads/mid-term examination.xlsx')
    table = data.sheet_by_name(u'Sheet1')
    for li in range(table.nrows):
        #print table.row(li)
        no = str(int(table.cell_value(li,0)))
        name = table.cell_value(li,1)
        score = str(table.cell_value(li,2))
        sendmail(name,'13210370002',score)
        time.sleep(1)
        break
        #print no,name,score

