import os.path
import json
import logging

from gnomeextensionssync.structs.extensionlist import extensionlist
from gnomeextensionssync.structs.extension import extension


class read:


    def __init__(self, config: str = ""):
        self.config = config
        self.extList = extensionlist()


    def read(self) -> bool:

        with open(self.config) as f:
            parsed = json.load(f)
            if not parsed['sync']['gnome-extensions']:
                logging.error("Bad format or missing gnome extensions")
                return False

            for cur in parsed['sync']['gnome-extensions']:
                ext = extension()
                ext.setUuid(cur['uuid'])
                ext.setName(cur['name'])
                ext.setEnabled(cur['enabled'])
                ext.setManualInstall(cur['manual'])

                if "settings" in cur:
                    ext.setSettings()
                    
                self.extList.add(ext)

        return True

            

    def getExtensionList(self):
        return self.extList
