import logging

from gnomeextensionssync.configs.write import write as writeconfig

from .extensioncommand import extensioncommand
from .extensionlist import extensionlist
from .parseinfo import parseinfo
from .parselist import parselist
from .writeconfig import writeconfig
from .readconfig import readconfig
from .dconfcommand import dconfcommand
from .gnomeurl import gnomeurl
from .parsejson import parsejson
from .gnomeshell import gnomeshell

class generate():

    def execute(self):

        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

        if conf == ".config/gnome-extensions-sync/extensions.json":
            confFile = os.environ['HOME'] + '/' + conf
            confPath = os.path.dirname(os.path.realpath(confFile))
            Path(confPath).mkdir(parents=True, exist_ok=True)


        cmd = extensioncommand()
        logging.debug("gnome-extensions version: {}".format(cmd.version()))
        logging.debug("Configuration file: {}".format(conf))
        
            # Get installed extensions
        userparse = parselist(cmd.userlist(), True)
        extList = userparse.getExtensionList()
        #sysparse = parselist(cmd.systemlist())

            # Write Configuration
        logging.debug("Writing configuration file")
        write = writeconfig(conf)
        write.setExtensionList(extList)
        write.write()
        logging.info("Generate complete")

