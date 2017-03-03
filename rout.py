# -*- coding: utf-8 -*-
# 重启路由器脚本
#
import urllib2, base64

def rerout():
    # IP for the router
    ip = '192.168.0.1'
    # 验证的用户名和密码
    login_user = 'admin'
    login_pw = 'admin'

    # 请求地址
    url = 'http://' + ip + '/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7'
    auth = 'Basic ' + base64.b64encode(login_user+':'+login_pw)
    print auth
    heads = { 'Referer' : 'http://' + ip + '/userRpm/SysRebootRpm.htm',
             'Authorization' : auth
    }
    
    # 请求重启路由器
    request = urllib2.Request(url, None, heads)
    response = urllib2.urlopen(request)
    print response.read()