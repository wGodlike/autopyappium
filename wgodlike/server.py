#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-09-07
# @Desc
import json
import multiprocessing
import os
import subprocess
import logging

from wgodlike import logger


class Server(object):

    def __init__(self, devices_list) -> None:
        self.devices_list = devices_list
        logger.Logger()
        super().__init__()

    @staticmethod
    def is_port_used(port_num):
        """
        :param port_num:
        :return:
        """
        command = 'netstat -an|grep ' + str(port_num)
        # result = os.popen(command).read()  # close()
        with os.popen(command, mode='r') as f:
            result = f.read()
        if not result:
            return True
        else:
            return False

    def generate_port_list(self, port_init, port_total):
        """
        :param port_init: int port初始值 最大值65535
        :param port_total: int
        :return:
        """
        port_list = []
        while len(port_list) != port_total:
            if self.is_port_used(port_init):
                port_list.append(port_init)
            port_init += 1
        with open('config/port.json', mode='w') as f:
            f.write(json.dumps(port_list))
        return port_list

    def get_command(self):
        cmd_list = []
        bootstrap_port_list = self.generate_port_list(20000, len(self.devices_list))
        appium_port_list = self.generate_port_list(10000, len(self.devices_list))
        for i, j, k in zip(appium_port_list, bootstrap_port_list, self.devices_list):
            command = ("appium --log-timestamp --local-timezone" +
                       " -p " + str(i) +
                       " -bp " + str(j) +
                       " -U " + k
                       )
            cmd_list.append(command)
        return cmd_list

    @staticmethod
    def appium_start(command, devices_name):
        subprocess.Popen(command, shell=True,
                         stdout=open('logs/appium_logs/' + devices_name + '.log', mode='a'),
                         stderr=subprocess.STDOUT)

    def start(self):
        os.system('killall node')  # mac  win: command="taskkill -F -PID node.exe"
        cmds = self.get_command()
        appium_process = []
        for i, j in zip(cmds, self.devices_list):
            appium = multiprocessing.Process(target=self.appium_start, args=(i, j))
            appium_process.append(appium)
        logging.info('开始启动appium服务')
        for appium in appium_process:
            appium.start()
        for appium in appium_process:
            appium.join()

        with open('config/port.json', mode='r') as f:
            appium_port_list = json.loads(f.read())
        for i, j in zip(appium_port_list, self.devices_list):
            if self.is_port_used(i):
                logging.info('设备{0}成功启动appium服务,port={1}'.format(j, i))


if __name__ == '__main__':
    l = ['111', '222']
    s = Server(l)
    s.start()
