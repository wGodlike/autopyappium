#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-07
# @Desc
import os
import json
import logging

from wgodlike import logger
from appium import webdriver


def appium_desired(port):
    # path = os.path.abspath(os.path.dirname(os.getcwd()))
    with open('config/desired_caps.json', mode='r') as f:
        desired_caps = json.loads(f.read())
    logger.Logger()
    logging.info('start creat driver...')
    try:
        driver = webdriver.Remote('http://127.0.0.1:' + port + '/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    with open('config/port.json', mode='r') as f:
        port_list = json.load(f)
    for p in port_list:
        drivers = appium_desired(p)

