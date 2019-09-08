#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-08
# @Desc
import time

from selenium.webdriver.support.wait import WebDriverWait

from wgodlike import logger
from wgodlike.base import Base


class Common(Base):

    def __init__(self, driver) -> None:
        # self.driver = driver
        self.log = logger.Logger()
        super().__init__(driver)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def switch(self, name):
        # 'WEBVIEW_com.wondershare.drfone'
        # 'NATIVE_APP'
        contexts = self.driver.contexts
        print(contexts)
        self.driver.switch_to.context(name)

    def get_toast(self):
        limit_message = "用户名或密码错误，你还可以尝试3次"
        message = '//*[@text=\'{}\']'.format(limit_message)
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
        print(toast_element.text)
        return toast_element.text

    def get_images(self, name):
        name = time.strftime('%Y%m%d_%H-%M-%S') + '_' + name
        self.driver.save_screenshot('logs/images/' + name + '.png')
        print(name)

    def swipe_to(self, direction):
        """
        :param direction: 指明滑动方向
        :return:
        """
        w = self.get_size()
        if direction is 'left':
            x1 = int(w[0] * 0.9)
            y1 = int(w[1] * 0.5)
            x2 = int(w[0] * 0.1)
            self.driver.swipe(x1, y1, x2, y1, 1500)
        elif direction is 'up':
            x1 = int(w[0] * 0.5)
            y1 = int(w[1] * 0.95)
            y2 = int(w[1] * 0.35)
            self.driver.swipe(x1, y1, x1, y2, 1000)
        elif direction is 'right':
            pass
        elif direction is 'up':
            pass
        else:
            self.log.logger.error('数据错误, 只支持 left、up、right、down')


if __name__ == '__main__':
    s = 'abc'
    print(s)
    s = time.strftime('%Y%m%d_%H-%M-%S') + '_' + s
    print(s)
