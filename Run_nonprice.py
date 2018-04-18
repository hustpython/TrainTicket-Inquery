'''@author: yzw
'''
#!/usr/bin/python  
# -*- coding:utf-8 -*- 
import json
from get_urltrain import d
import urllib
from urllib import request
import requests
from pprint import pprint
from get_urltrain import url
from prettytable import PrettyTable
from color_set import colored

r = requests.get(url, verify=False)
rows = r.json()["data"]["result"]
stamap = r.json()["data"]["map"]
trains= PrettyTable()
trains.field_names=["车次","车站","时间","历时","商务座","特等座","一等座","二等座","高级软卧","软卧","硬卧 ","软座 ","硬座","无座"]
num = len(rows)
# 关于票价的信息隐藏的比较深，row = row.split('|')，解析出来。如下，具体对应座位关系没有具体研究。
# '20180419', '3', 'N2', '01', '06', '0', '0', '', '', '', '', '', '', '', '', '', '',
# '有', '有', '11', '', 'O0M090', 'OM9', '1'
for row in rows :
    row = row.split('|')
    trains.add_row([row[3],
                   '\n'.join([colored('green', stamap[row[6]]),
                   colored('red', stamap[row[7]])]),
                   '\n'.join([colored('green', row[8]),
                   colored('red', row[9])]),
                   row[10],1,2,
                   3,4,5,
                   6,7,8,
                   9,10])
print ('查询结束，共有 %d 趟列车。'%num )
print (trains)

