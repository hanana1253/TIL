#!/usr/bin/env python3

# -*- coding:utf-8 -*-


num = int(input('몇 명을 먹이고자 하는고?'))


if num <= 2:
    result = '당연히 {}마리, 1인 1닭의 미덕을 지키거라'.format(num)
else:
    result = '아직 만드는 중'

print(result)

