#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-08
# @Desc
import yaml
from selenium.webdriver.common.by import By


def get_locator(key):
    with open('config/elements.yaml', mode='r') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
    by_type = res.get(key).split('>')[0]
    by_val = res.get(key).split('>')[1]
    if by_type == 'id':
        print(by_val)
        return
    elif by_type == 'xpath':
        print(by_val)
    else:
        print('输入类型无效')


if __name__ == '__main__':
    s = '123'
    s.split()
    print(get_locator('gobtn'))

