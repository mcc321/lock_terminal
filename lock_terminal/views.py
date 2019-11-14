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
                    # 开锁驱动
                    return jsonify({"info":"success"})
                elif dic['condition']=='off':
                    # 关锁驱动
                    return jsonify({"info":"success"})
                else:
                    return jsonify({"info":"fail"})
            except:
                return jsonify({"info":"fail"})
        else:
            return jsonify({"info":"fail"})
    else:
        return jsonify({"info":"fail"})

