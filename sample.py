# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install request`
import json, sys, time

# 云小微平台申请的appkey和appAccesstoken，请填入自己的
appkey = "xxx";
appAccessToken = b"xxx";

usage = '''
####
#   usage:
#   python nlp.py Text
#   Text, 需要NLP的文本
####
'''
# ***** Task 1: 拼接请求数据和时间戳 *****

## 获取请求数据(也就是HTTP请求的Body)
postData = '''
{
    "baseInfo":
    {
        "qua": "QV=3&PL=ADR&VE=7.6&VN=0.0.0.1&PP=com.tencent.xxx",
        "user":
        {
            "user_id": "",
            "account":{
                "id":"",
                "token":"",
                "appid":"",
                "type":""
            }
        },
        "lbs":
        {
            "latitude":30.5434,
            "longitude":104.068
        },
        "device":{
            "serialNum":"deviceSerialNum"
        }
    },
    "context":[
        
        {"header":{"name":"ShowState","namespace":"TvsUserInterface"},"payload":{"isEnabled":true}}
        
    ],
    "event":
    {
       "header": {
			"namespace": "TvsTextRecognizer",
			"name": "Recognize",
			"messageId": "messageId1",
			"dialogRequestId": "dialo33g3Resssdddddsdssqud3233332dessssstId122"
		},
		"payload": {
            "text":""
        }
    }
}
'''

jsonReq = json.loads(postData);

jsonReq["event"]["payload"]["text"] = "天气怎么样";

## 使用requests.session保持长连接
session = requests.session()

## 获得ISO8601时间戳
credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

## 拼接数据
signingContent = json.dumps(jsonReq) + credentialDate

# ***** Task 2: 获取Signature签名 *****
signature = hmac.new(appAccessToken, signingContent.encode('utf-8'), hashlib.sha256).hexdigest()

# ***** Task 3: 在HTTP请求头中带上签名信息
authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + appkey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature
headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader}

# **** Send the request *****
requestUrl = 'https://aiwx.html5.qq.com/api/v2/event'
 

print ('Begin request...')
print ('Request Url = ' + requestUrl)


session.headers.update(headers)
print ('Request Headers =' + str(session.headers))
print ('Request Body =' + json.dumps(jsonReq))

reqTime = time.time();
r = session.post(requestUrl, data = json.dumps(jsonReq).encode('utf-8'))
respTime = time.time();

print ('Response...')
print ("HTTP Status Code:%d" % r.status_code, "cost:%f(ms)" %((respTime - reqTime) * 1000));
print (r.text)


jsonResp = json.loads(r.text);


js = json.dumps(jsonResp, sort_keys=True, indent=4, separators=(',', ':'))
print(js)
