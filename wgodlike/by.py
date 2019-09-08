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
    if by_type is 'id':
        el = (By.ID, by_val)  # drive.find_element(el).click()
        return el
    elif by_type is 'xpath':
        el = (By.XPATH, by_val)
        return el
    else:
        print('输入类型无效')


"""
# 导入By
from selenium.webdriver.common.by import By
# id定位
find_element(By.ID, "id值")
# name属性定位
find_element(By.NAME, "name值")
# class属性定位
find_element(By.CLASS_NAME, "class值")
# 标签定位
find_element(By.TAG_NAME, "input")
#定位链接
find_element(By.LINK_TEXT, "新闻")
# 定位长链接
find_element(By.PARTIAL_LINK_TEXT, "新")
# xpath定位
find_element(By.XPATH, "//*[@class='值']")
# css定位
find_element(By.CSS_SELECTOR, "span.class值>input#值")
"""

if __name__ == '__main__':
    s = 'ABCD'
    s.split()
    print(s is 'ABCD')
    # print(get_locator('gobtn'))

