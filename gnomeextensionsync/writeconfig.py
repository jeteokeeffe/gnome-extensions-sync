import yaml
import os


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
        extyaml = []
        for ext in self.extlist.getAll():
            if ext.getManualInstall():
                extdata = { 'name' : ext.getName(),
                    'uuid': ext.getUuid(),
                    'url': ext.getUrl(),
                    'enabled': ext.getEnabled(),
                    'manual': ext.getManualInstall(),
                }
                extyaml.append(extdata)


        data = {
            'sync': {
                'gnome-extensions': extyaml
            }
        }


            # Check if path is writable
        os.path.exists(self.config)

            # Check if writable
        os.access(self.config, os.W_OK)

            # Open as writable
        try:
            with open(self.config, 'w') as f:
                result = yaml.dump(data, f)
        except IOError as e:
            print("error")

        return True

