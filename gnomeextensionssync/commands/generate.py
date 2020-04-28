import logging
import os
from pathlib import Path

from gnomeextensionssync.commands.command import command
from gnomeextensionssync.configs.write import write as writeconfig

from gnomeextensionssync.extensioncommand import extensioncommand
from gnomeextensionssync.structs.extensionlist import extensionlist
from gnomeextensionssync.parseinfo import parseinfo
from gnomeextensionssync.parselist import parselist
from gnomeextensionssync.dconfcommand import dconfcommand
from gnomeextensionssync.gnomeurl import gnomeurl
from gnomeextensionssync.parsejson import parsejson
from gnomeextensionssync.gnomeshell import gnomeshell

class generate(command):

    def __init__(self):
        super().__init__()

    def execute(self):

        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

        if self.conf.endswith(".config/gnome-extensions-sync/extensions.json"):
            confPath = os.path.dirname(os.path.realpath(self.conf))
            Path(confPath).mkdir(parents=True, exist_ok=True)


        cmd = extensioncommand()
        logging.debug("gnome-extensions version: {}".format(cmd.version()))
        logging.debug("Configuration file: {}".format(self.conf))
        
            # Get installed extensions
        userparse = parselist(cmd.userlist(), True)
        extList = userparse.getExtensionList()
        #sysparse = parselist(cmd.systemlist())

            # Write Configuration
        logging.debug("Writing configuration file")
        write = writeconfig(self.conf)
        write.setExtensionList(extList)
        write.write()
        logging.info("Generate complete")

