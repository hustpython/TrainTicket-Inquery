#coding:utf8

from station import stations
import warnings

#f1= input('请输入起始城市：\n')
f1="武汉"
f = stations[f1]

#t1= input('请输入目的城市：\n')
t1 = "北京"
t = stations[t1]


#d1=input('请输入出发时间： \n')
d1 = "04-19"
d=str('2018-')+str(d1)
print ('正在查询'+f1+'至'+t1+'的列车，请听听音乐...')



url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+d+'&leftTicketDTO.from_station='+f+'&leftTicketDTO.to_station='+t+'&purpose_codes=ADULT'
warnings.filterwarnings("ignore")