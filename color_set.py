'''@author: yzw
'''
#!/usr/bin/python  
# -*- coding:utf-8 -*-  

def colored(color, text):
    table = {
        'red': '\033[91m',
        'green': '\033[92m',
        # no color
        'nc': '\033[0m'
    }
    cv = table.get(color)
    nc = table.get('nc')
    return ''.join([cv, text, nc])