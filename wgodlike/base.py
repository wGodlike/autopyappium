#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-08
# @Desc


class Base(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()

    def find_element(self, *args):
        return self.driver.find_element(*args)
