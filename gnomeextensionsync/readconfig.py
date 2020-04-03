import yaml
import os.path

from .extensionlist import extensionlist
from .extension import extension


class readconfig:


    def __init__(self, config: str = ""):
        self.config = config
        self.extList = extensionlist()



    def read(self):

        with open(self.config) as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for sync in data:
                for cur in sync['sync']['gnome-extensions']:
                    ext = extension()
                    ext.setUuid(cur['uuid'])
                    ext.setName(cur['name'])
                    ext.setEnabled(cur['enabled'])
                    ext.setManualInstall(cur['manual'])
                    self.extList.add(ext)


            

    def getExtensionList(self):
        return self.extList
