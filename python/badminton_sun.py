#!/usr/bin/python
# -*- coding: utf-8 -*-
#script for badminton version 1.0.3 2013/08/26 14:00
import requests,re,urllib,sys,time
import datetime
#username 学号/工号
username='32086'
#name 名字必须是utf-8
#张校捷 翁经纬 李振华
name='翁经纬'
password='QSLLXFX5'
#mobile 手14
mobile='13761571639'
#定的起始时间，定一个小时，整数
ordertime=13
#ordertime=14
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20130626 Firefox/17.0 Iceweasel/17.0.7',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
           'Connection':'keep-alive','DNT':'1'}
myheader={'Host':'www.elife.fudan.edu.cn','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3','Accept-Encoding':'gzip, deflate','Referer':'http://www.portal.fudan.edu.cn/applyBaseView.do?applyId=178651','Connection':'keep-alive'}
class orderplace:
    s=requests.session()
    item='北区体育馆羽毛球'
#    item='正大体育馆羽毛球'
    myheader={'Host':'www.elife.fudan.edu.cn','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3','Accept-Encoding':'gzip, deflate','Referer':'http://www.portal.fudan.edu.cn/applyBaseView.do?applyId=178651','Connection':'keep-alive'}
    mailserver={}
    def __init__(self,username,password,name,mobile,starttime):
        self.username=username
        self.password=password
        self.name=name
        self.mobile=mobile
        self.starttime=starttime
        self.endtime=starttime+1
        return
    def nextDay(self,day):
        today=datetime.datetime.today()
        todayAtThreeAm=datetime.datetime(today.year, today.month, today.day, 3)
        nextweekdayAtThreeAM=todayAtThreeAm+datetime.timedelta(7)
        nextdayAtThreeAm=nextweekdayAtThreeAM+datetime.timedelta(day-today.isoweekday())
        return nextdayAtThreeAm.strftime('%Y-%m-%d')
    def nextSaturday(self):
        return self.nextDay(6)
    def loginportal(self):
        logindata={'email':self.username,'password':self.password}
        loginpage='http://www.portal.fudan.edu.cn/main/login.do?invitationCode='
        t=self.s.post(loginpage,logindata,verify=False)
        return
    def visit_order_page(self):
        orderpage='http://www.portal.fudan.edu.cn/applyBaseView.do?applyId=178651'
        t=self.s.get(orderpage,verify=False)
        re_mainpage=re.compile('(?<=main src=\").*?(?=\")')
        self.redirectpage=re_mainpage.search(t.text.encode('utf-8')).group()
        self.serviceCategoryid=self.redirectpage.split('=')[-1]
        return
    def parse_order_page(self):
        t=self.s.get(self.redirectpage,verify=False,allow_redirects=True)
#t=s.get(redirectpage,verify=False,allow_redirects=True)
        order_content=t.text.encode('utf-8')
        bqbmtnstart=order_content.index(self.item)
        bqbmtnstart_content=order_content[bqbmtnstart:]
        bqbmtnend=bqbmtnstart_content.index('立即预订')
        bqbmtn_content=bqbmtnstart_content[:bqbmtnend]
        re_order_url=re.compile('(?<=href=\").*?(?=\")')
        self.order_url='http://www.elife.fudan.edu.cn'+re_order_url.search(bqbmtn_content).group()
        self.serviceContentid=self.order_url.split('=')[-1]
        return
    def visit_badminton_date_selection(self):
        self.endtime=self.starttime+1
        t=self.s.get(self.order_url,verify=False,allow_redirects=True,headers=self.myheader)
        # print serviceCategoryid
        # print serviceContentid
        # date_query_body={'currentDate':self.nextSaturday()}
        t=self.s.get(self.order_url+'&currentDate=%s'%self.nextSaturday(),verify=False,allow_redirects=True,headers=self.myheader)
        order_day_content=t.text.encode('utf-8')
        serviceResourceIDstart=order_day_content.find('<font>%s:00'%self.starttime)
        rest_content=order_day_content[serviceResourceIDstart:]
        serviceResourceIDend=rest_content.find('<font>%s:00'%(self.endtime))
        serviceResourceIDcontent=rest_content[:serviceResourceIDend]
        re_service_resourceid=re.compile('(?<=checkUser\(\').*?(?=\')')
        serviceResourceIDcontentresult=re_service_resourceid.search(serviceResourceIDcontent)
        if serviceResourceIDcontentresult==None:
            return False
        else:
            self.serviceResourceid=re_service_resourceid.search(serviceResourceIDcontent).group()
            return True
# print serviceResourceid
        return
    def makeorder(self):
        body={'serviceResource.id':self.serviceResourceid}
        check_url='http://www.elife.fudan.edu.cn/ordinary/meta/serviceResourceAction!timesLimit.action?serviceCateGory.id=&beginTime=%s:00&endTime=%s:00'%(self.starttime,self.endtime)
        t=self.s.post(check_url,body,verify=False,allow_redirects=True,headers=self.myheader)
        body={'serviceContent.id':self.serviceContentid,'serviceCategory.id':self.serviceCategoryid,'serviceResource.id':self.serviceResourceid}
        confirm_url='http://www.elife.fudan.edu.cn/order/meta/porder!loadOrderForm_ordinary.action?'+urllib.urlencode(body)
        t=self.s.get(confirm_url,verify=False,allow_redirects=True,headers=self.myheader)
# print t.text
        return
    def submitpersonalcontact(self):
        body={'beginTime':self.starttime,'endTime':self.endtime,'orderuser':self.name,'serviceCategory.id':self.serviceCategoryid,'serviceContent.id':self.serviceContentid,'serviceOrders.appointTime':self.nextSaturday(),'serviceOrders.department':'化学系','serviceOrders.mobile':self.mobile,'serviceOrders.note':'','serviceOrders.phone':'021','serviceResource.id':self.serviceResourceid}
        confirm_url='http://www.elife.fudan.edu.cn/order/meta/porder!doSave.action?op=order'
        self.s.post(confirm_url,body,verify=False,allow_redirects=True,headers=self.myheader)
        print 'Succeed in appointing %s from %s to %s'%(self.item,self.starttime,self.endtime)
        return
    def checkorder(self):
        check_order_url='http://www.elife.fudan.edu.cn/pcenter/orderflow/userBoxAction.action'
        t=self.s.get(check_order_url,verify=False,allow_redirects=True)
        check_order_content=t.text.encode('utf-8')
# print check_order_content
        order_start=check_order_content.find('table3_tr_td1')
        rest_content=check_order_content[order_start:]
        order_end=rest_content.find('待签到')
        if order_end==-1:
            return True
        order_info=rest_content[:order_end]
        if order_info.find(self.item)>-1:
            order_no=re.search('\d{9}',order_info).group()
            order_date=re.search('\d+-\d+-\d+',order_info).group()
            if order_date==self.nextSaturday():
                print 'you have an apointment at %s, order no: %s'%(order_date,order_no)
                return False
            else:
                return True
        else:
            return True
    def flow(self):
        self.loginportal()
        if self.checkorder() or True :
        #if True :
            self.visit_order_page()
            self.parse_order_page()
            self.date_available=False
            for i in range(60):
                if self.visit_badminton_date_selection():
                    self.makeorder()
                    self.submitpersonalcontact()
                    return
                if i%6==0:
                    print '%s from %s to %s of %s is not available now.'%(self.item,self.starttime,self.endtime,self.nextSaturday())
                    time.sleep(5)
if __name__=='__main__':
    # orderpage()
    test=orderplace(username,password,name,mobile,ordertime)
    test.flow()
