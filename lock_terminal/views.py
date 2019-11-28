# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/13
@file: views.py
@function:
@modify:
"""

from .libs import get_json,jsonify,post_data
import random
import string
from django.shortcuts import render
from .unlock import unlock
import os
import time

def index(request):
    return render(request,'index.html')


def condition(request):
    dic=get_json(request)
    with open('passwd.txt', 'r') as file:
        old_passwd=file.readline()
    if "passwd" in dic:
        if old_passwd==dic['passwd']:
            new_passwd = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            post_data({"new_passwd":new_passwd})
            with open('passwd.txt', 'w') as file:
                file.write(new_passwd)
            try:
                if dic['condition']=='on':
                    unlock()
                    return jsonify({"info":"success"})
                elif dic['condition']=='off':
                    # 关锁驱动
                    return jsonify({"info":"success"})
                else:
                    return jsonify({"info":"fail",'tip':'请求参数错误'})
            except:
                return jsonify({"info":"fail",'tip':'锁故障'})
        else:
            return jsonify({"info":"fail",'tip':'密码校验错误'})
    else:
        return jsonify({"info":"fail",'tip':'请求错误'})

def get_image(request):
    dic=get_json(request)
    with open('passwd.txt', 'r') as file:
        old_passwd=file.readline()
    if "passwd" in dic:
        if old_passwd==dic['passwd']:
            new_passwd = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            post_data({"new_passwd":new_passwd})
            with open('passwd.txt', 'w') as file:
                file.write(new_passwd)
            try:
                r = {'pic':[]}
                dir = "/root/lock/templates/camera"
                url_prefix="https://proxy.wyt.cloud/templates/camera/"
                docs=[d for d in os.listdir(dir)]
                for doc in docs:
                    url=url_prefix+doc
                    do=dir+'/'+doc
                    timestamp=os.path.getmtime(do)
                    t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
                    r['pic'].append({"time":t,"image":url})
                return jsonify(r)
            except:
                return jsonify({"info":"fail",'tip':'锁故障'})
        else:
            return jsonify({"info":"fail",'tip':'密码校验错误'})
    else:
        return jsonify({"info":"fail",'tip':'请求错误'})

