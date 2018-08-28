#coding:utf-8
#author:Blood_Zer0
#file:http_auth_dict.py
#time:2017/2/16 上午10:27


import base64
import sys

def judge_file(self):
    try:
        open(self,'r')
    except IOError as e:
        print "can't find file"
        exit()

def judge_opt():
    if(len(sys.argv) == 4):
        pass
    else:
        print "usage:python http_auth_dict.py user_file pass_file new_dict_file"

if __name__ == "__main__":
    judge_opt()
    judge_file(sys.argv[1])
    judge_file(sys.argv[2])
    tmp = []
    for username in open(sys.argv[1]).readlines():
        for password in open(sys.argv[2]).readlines():
            # print username.strip(),password.strip()
            tmp.append("Basic " + base64.b64encode(username.strip() + ":" + password.strip()) + '\n')

    new_file = open(sys.argv[3],'w+')
    new_file.writelines(tmp)