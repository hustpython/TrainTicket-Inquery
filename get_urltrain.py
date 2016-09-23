#coding:utf8

from station import stations
import warnings

f1= input('请输入起始城市：\n')
f = stations[f1]

t1= input('请输入目的城市：\n')
t = stations[t1]


d1=input('请输入出发时间： \n')
d=str('2016-')+str(d1)
print ('正在查询'+f1+'至'+t1+'的列车，请听听音乐...')



url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+d+'&from_station='+f+'&to_station='+t
warnings.filterwarnings("ignore")