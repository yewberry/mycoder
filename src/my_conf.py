# -*- coding: utf-8 -*-
import os
import ConfigParser
from my_glob import LOG

CFG_STR = """[GENERAL]
version=1.0.0
"""

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyConf(object):
    __metaclass__ = Singleton

    def __init__(self, file_path=""):
        LOG.info(u"settings.ini path:{}".format(file_path))
        self.cfgPath = file_path
        if file_path == "":
            LOG.error("cfg file path is empty which shouldn't happen")
        elif not os.path.isfile(file_path):
            with open(self.cfgPath, "w") as f:
                f.write(CFG_STR)

    def get(self, sect, name):
        config = ConfigParser.ConfigParser()
        config.read(self.cfgPath)
        if not config.has_option(sect, name):
            return None
        return config.get(sect, name)

    def set(self, sect, name, value):
        config = ConfigParser.ConfigParser()
        config.read(self.cfgPath)
        if not config.has_section(sect):
            config.add_section(sect)
        config.set(sect, name, value)
        config.write(open(self.cfgPath, "r+"))

