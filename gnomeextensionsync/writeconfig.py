import os
import json
import logging


from .extensionlist import extensionlist


class writeconfig:
    """
    Create gnome extensions configuration file
    """


    def __init__(self, config = ""):
        self.extlist = extensionlist()
        self.config = config


    def setExtensionList(self, extlist: extensionlist):
        self.extlist = extlist


    def write(self):

            # Extensions
        extArr = []
        for ext in self.extlist.getAll():
            if ext.getManualInstall():

                    # Extension Details
                extData = { 'name' : ext.getName(),
                    'uuid': ext.getUuid(),
                    'url': ext.getUrl(),
                    'enabled': ext.getEnabled(),
                    'manual': ext.getManualInstall(),
                }

                    # Check if Extension has settings
                settings = ext.getSettings()
                if len(settings) > 0:
                    extData["settings"] = []

                extArr.append(extData)



        data = {
            'sync': {
                'gnome-extensions': extArr
            }
        }

            # Check if path is writable
        os.path.exists(self.config)

            # Check if writable
        os.access(self.config, os.W_OK)

            # Open as writable
        try:
            with open(self.config, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logging.error("Failed to write configuration file")
            return False

        return True


