#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-07
# @Desc
import os
import json

from appium import webdriver


class Driverinit(object):

    def __init__(self) -> None:
        super().__init__()

    def init(self):
        path = os.path.abspath(os.path.dirname(os.getcwd()))
        with open(path + '/config/desired_caps.json', mode='r') as f:
            desired_caps = json.loads(f.read())
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    pass
