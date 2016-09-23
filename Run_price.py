'''@author: yzw
'''
#!/usr/bin/python  
# -*- coding:utf-8 -*- 
import re
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
rows = r.json()['data']['datas']
trains= PrettyTable()
#header = '车次 车站 时间 历时 商务座/价格 特等座/价格  一等座/价格  二等座/价格  高级软卧/价格  软卧/价格   硬卧/价格  软座/价格  硬座/价格  无座/价格 '.split()
trains.field_names=["车次","车站","时间","历时","商务座/价格","特等座/价格","一等座/价格","二等座/价格","高级软卧/价格","软卧/价格","硬卧/价格 ","软座/价格 ","硬座/价格","无座/价格"]
trains.align["车次"] = "l"
trains.padding_width = 2
num = len(rows)

for row in rows :
 
    url_price ="https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no="+row['train_no']+"&from_station_no="+row['from_station_no']+"&to_station_no="+row['to_station_no']+"&seat_types="+row['seat_types']+"&train_date="+d
    req = urllib.request.Request(url_price)
    r_price = urllib.request.urlopen(req).read().decode('utf-8')

    r_price = json.loads(r_price)
    price = r_price['data']
    price = dict(price)
    #SWZ
    try:
        A = ('A9' in price.keys())
        if A == False :
           A =''
        else:
           A =price['A9']
        
        #TDZ
        B = ('P' in price.keys())
        if B == False :
           B =''
        else:
           B =price['P']
        
        #YDZ
        C = ('M' in price.keys())
        if C == False :
           C =''
        else:
           C =price['M']
        #EDZ
        D = ('O' in price.keys())
        if D == False :
           D =''
        else:
           D =price['O']
        #GJRW
        E = ('A6' in price.keys())
        if E == False :
           E =''
        else:
           E =price['A6']
        #RW
        F = ('A4' in price.keys())
        if F == False :
           F =''
        else:
           F =price['A4']
        #YW
        G = ('A3' in price.keys())
        if G == False :
           G =''
        else:
           G =price['A3']
        #RZ
        H = ('A2' in price.keys())
        if H == False :
           H =''
        else:
           H =price['A2']
        #YZ
        I = ('A1' in price.keys())
        if I == False :
           I =''
        else:
           I =price['A1']
        #WZ
        J = ('WZ' in price.keys())
        if J == False :
           J =''
        else:
           J =price['WZ']
        trains.add_row([row['station_train_code'],
                   '\n'.join([colored('green', row['from_station_name']),
                   colored('red', row['to_station_name'])]),
                   '\n'.join([colored('green', row['start_time']),
                   colored('red', row['arrive_time'])]),
                   row['lishi'],
                   colored('green',row['swz_num'])+'\n'+A,
                   colored('green',row['tz_num'])+'\n'+B,
                   colored('green',row['zy_num'])+'\n'+C,
                   colored('green',row['ze_num'])+'\n'+D,
                   colored('green',row['gr_num'])+'\n'+E,
                   colored('green',row['rw_num'])+'\n'+F,
                   colored('green',row['yw_num'])+'\n'+G,
                   colored('green',row['rz_num'])+'\n'+H,
                   colored('green',row['yz_num'])+'\n'+I,
                   colored('green',row['wz_num'])+'\n'+J])
    except(TypeError, IndexError):
        pass 
print ('查询结束，共有 %d 趟列车。'%num )
print (trains)

