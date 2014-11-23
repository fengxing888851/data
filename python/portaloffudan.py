#! /usr/bin/python  
  
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  
hosturl = 'https://uis2.fudan.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fwww.portal.fudan.edu.cn%2Fapply%2FisRecommendApplyShow.do' 
posturl = 'http://www.portal.fudan.edu.cn/main/login.do?invitationCode=' 
  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener) ### opener.open(posturl).read()  #replace this line, due to install_opener,we can use urllib2.urlopen 
  
h = urllib2.urlopen(hosturl)  
  
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',  
           'Referer' : 'http://www.portal.fudan.edu.cn/main/loginIndex.do?ltype=1'}  
postData = {'email' : '13210370002',  
            'password' : '175815',  
            }  
  
postData = urllib.urlencode(postData)  
  
request = urllib2.Request(posturl, postData, headers)
print request  
response = urllib2.urlopen(request)  
text = response.read()  
##print text  
print cj
for c in cj:
	print c.name,':',c.value


##from lxml import etree  
##import mechanize  
#import lxml.html  
##import cookielib  
#  
##br = mechanize.Browser()  
##r = br.open('http://yourdomain.com')  
##html = br.response().read()  
##root = lxml.html.fromstring(html)  
##divs = root.xpath("//div[@class='test']")  
#hparser = etree.HTMLParser(encoding='utf-8') #for avoiding unicode codec problems  
#htree = etree.parse('http://yourdomain.com',hparser)  
#htree.write('/tmp/bi.html')   
#divs= htree.xpath("//div[@class='test']")  
