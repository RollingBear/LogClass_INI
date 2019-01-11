# -*- coding: utf-8 -*-

# 2019/1/11 0011 上午 10:29     

__author__ = 'RollingBear'


import os
import configparser


class Dictionary(dict):

    '''把 config.ini中的参数添加到dict'''

    def __getattr__(self, keyname):
        # key不存在返回默认值
        return self.get(keyname, "config.ini中没有找到对应的keyname")


class Config(object):

    '''ConfigParser二次封装， 在字典中获取value'''

    def __init__(self):
        # 设置conf.ini路径
        current_dir = os.path.dirname(__file__)
        top_one_dir = os.path.dirname(current_dir)
        file_name = top_one_dir + "\\conf\\conf.ini"
        # 实例化ConfigParser对象
        self.config = configparser.ConfigParser()
        self.config.read(file_name)
        # 根据section把key、value写入字典
        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for keyname, value in self.config.items(section):
                setattr(getattr(self, section), keyname, value)


    def getconf(self, section):
        if section in self.config.sections():
            pass
        else:
            print('config.ini 找不到该 seciont')
        return getattr(self, section)