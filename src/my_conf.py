# -*- coding: utf-8 -*-
import os
import ConfigParser
from my_glob import Singleton
from my_glob import LOG

CFG_STR = """[GENERAL]
VER=1.0.0
"""

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
        with open(self.cfgPath, "r") as f:
            config.readfp(f)
        return config.get(sect, name)

    def set(self, sect, name, value):
        config = ConfigParser.ConfigParser()
        with open(self.cfgPath, "w+") as f:
            config.readfp(f)
            config.set(sect, name, value)
            config.write(f)

