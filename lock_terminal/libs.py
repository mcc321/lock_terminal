# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/13
@file: libs.py
@function:
@modify:
"""

import simplejson
import requests
from django.http import HttpResponse
import logging
import base64
from Crypto.Cipher import AES
from django.conf import settings


def pad(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text


def mcc_print(info):
    logger = logging.getLogger('django')
    logger.info('=================================================================================================')
    logger.info(info)
    logger.info('=================================================================================================')


def get_json(request):
    return simplejson.loads(request.body.decode())


def post_data(dic):
    with open('passwd.txt','r') as file:
        old_passwd=file.readline()
        dic['old_passwd']=old_passwd
    r = requests.post(settings.API_URL, data=simplejson.dumps(dic))
    return simplejson.loads(r.text)


def jsonify(dic):
    return HttpResponse(simplejson.dumps(dic), content_type="application/json")


def encrypt(data,key,iv):
    iv = pad(iv).encode('utf-8')
    data = pad(data).encode('utf-8')
    key=pad(key).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    r = cipher.encrypt(data)
    return str(base64.encodebytes(r), encoding='utf-8')


def decrypt(encrypted_data,key,iv):
    key = pad(key).encode('utf-8')
    iv=pad(iv).encode('utf-8')
    encrypted_data = base64.decodebytes(encrypted_data.encode(encoding='utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = str(cipher.decrypt(encrypted_data), encoding='utf-8').replace('\0', '')
    return decrypted
