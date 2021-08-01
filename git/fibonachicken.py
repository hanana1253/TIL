#!/usr/bin/env python3

# -*- coding:utf-8 -*-


num = int(input('몇 명을 먹이고자 하는고?'))

if num <= 2:
    print('당연히 {}마리, 1인 1닭의 미덕을 지키거라'.format(num))
elif num % 3 == 0:
    result = (num * 2) / 3 
elif num % 2 == 0:
    result = num / 2 + 1
else:
    result = '아직 하는 중'

print('{}'.format(result))

