from multiprocessing import Process
import urllib2,urllib,cookielib,socket,httplib
import sys,datetime,random,time,logging
username='32086'
password='QSLLXFX5'
class webtype:
    username=''
    passwd=''
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
               'Connection':'keep-alive','DNT':'1'}
    bodies = {}
    loginpage='https://uis2.fudan.edu.cn/amserver/UI/Login'
    orderpage='http://www.portal.fudan.edu.cn/applyBaseView.do?applyId=178651'
    def __init__(self,username,passwd):
        self.username=username
        self.passwd=passwd
        self.cookiefile='fduuis_%s'%(self.username)
        self.cj = cookielib.LWPCookieJar(self.cookiefile)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        try:
            self.cj.load(self.cookiefile,ignore_discard=True,ignore_expires=True)
        except:
            print 'error'
        return
    def _request(self, url, time=3, intmout=10,bodies = {}, headers = {}):
        request = urllib2.Request(url,urllib.urlencode(bodies),headers=headers)
        result=''
        try:    
            result=self.opener.open(request).read()
        except urllib2.URLError as e:
            if time>0:
                result=self._request(url,time-1)
            else:
                result=''
            #print type(e)
        except socket.timeout as e:
            if time>0:
                result=self._request(url,time-1)
            else:
                result=''
            #print type(e)
        except (IOError, httplib.HTTPException) as e:
            result=''
            #print type(e)
        return result

    def login_fdu(self):
        content=self._request(self.loginpage,self.bodies,self.headers)
        self.bodies.update({'IDToken0':'','IDToken1':self.username,'IDToken2':self.passwd,'IDButton':'Submit','goto':'','encoded':'false','inputCode':'','gx_charset':'UTF-8'})
        self.headers.update({'Referer':'https://uis2.fudan.edu.cn/amserver/UI/Login?gx_charset=UTF-8'})
        content=self._request(self.loginpage,self.bodies,self.headers)
        self.cj.save(self.cookiefile,ignore_discard=True,ignore_expires=True)
        return
    def order(self):
        content=self._request(self.orderpage,self.bodies,self.headers)
        print content
        content=self._request('https://uis2.fudan.edu.cn/amserver/console',self.bodies,self.headers)
         print content
        return

        
if (__name__=='__main__'):
    a=webtype(username,password)
    a.login_fdu()
    a.order()

