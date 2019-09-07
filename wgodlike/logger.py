#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-08
# @Desc
import logging
import logging.config
import os


class Logger(object):

    def __init__(self) -> None:
        self.con_log = 'config/logger.conf'
        logging.config.fileConfig(self.con_log)
        self.logger = logging.getLogger()
        super().__init__()


if __name__ == '__main__':
    print(os.path.dirname(os.getcwd()))
