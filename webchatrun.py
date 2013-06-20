# -*- coding:utf8 -*-
import web
import hashlib
import xml.etree.cElementTree as ET
urls = (
    '/weixin','index'
)
class index(object):
    def GET(self):
      token='thome'
	    sign = web.input()
	    tmplist = [token,sign.timestamp,sign.nonce]
	    tmplist.sort()
	    tmpstr = "%s%s%s"%tuple(tmplist)
	    tmpstr = hashlib.sha1(tmpstr).hexdigest()
	    if tmpstr == sign.signature:
		    return sign.echostr
	    else:
		    return None
            
    def POST(self):
	    str_xml  = web.data()
	    xml = ET.fromstring(str_xml)
	    self.tname = xml.find('ToUserName').text
	    self.fname = xml.find('FromUserName').text
	    self.ctime = xml.find('CreateTime').text
	    self.mtype = xml.find('MsgType').text
	    content = xml.find('Content').text
	    mid   = xml.find('MsgId').text
            return self.Response()   

    def Response(self):
    	    textTpl = """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>

             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>"""
            echostr = textTpl % (self.fname,self.tname,self.ctime,self.mtype,'KXKKDSK')
            return echostr 

app = web.application(urls,globals())
application = app.wsgifunc()
