import logging
import os


class command():

    def __init__(self):
        self.dryrun = False

        self.conf = os.environ['HOME'] + '/' + '.config/gnome-extensions-sync/extensions.json'

    def setConfig(self, conf):
        if not conf.endswith(".config/gnome-extensions-sync/extensions.json"):
            self.conf = conf

