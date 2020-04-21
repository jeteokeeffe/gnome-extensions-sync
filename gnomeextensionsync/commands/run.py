import logging

from gnomeextensionssync.configs.read import read as readconfig

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


class run(command):

    def __init__(self):
        super().__init__()

    def execute(self):

        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

        gnomeShell = gnomeshell()
        logging.debug("gnome-shell version: {}".format(gnomeShell.getVersion()))
        gnomeCmd = extensioncommand()
        logging.debug("gnome-extensions version: {}".format(gnomeCmd.version()))
        logging.debug("Configuration file: {}".format(conf))

            # Read Configuration file
            # Get Expected List of Extensions
        read = readconfig(conf)
        read.read()
        expectedList = read.getExtensionList()

            # Get Installed Extensions
        userparse = parselist(gnomeCmd.userlist(), True)
        installedList = userparse.getExtensionList()

        
            # Sync Extensions
        for ext in expectedList.getAll():

                # https://docs.python.org/3/library/tempfile.html

                # Check Extension Exists
            logging.debug("Checking if extension already exists")
            if not installedList.exists(ext.getUuid()):

                    # Info on Extension
                output = gnomeurl.info(ext.getUuid())
                pj = parsejson()
                pj.parse(output)
                extVersion = pj.getVersion(gnomeShell.getMajorVersion())
                extZipFile = "/tmp/jete.zip"

                    # Check Compatible for Gnome


                if extVersion == False:
                    logging.warn("No compatible version found")
                else:
                        # Download Zip
                    logging.info("Downloading extension (ver: {})".format(extVersion))
                    gnomeurl.download(ext.getUuid(), extVersion, extZipFile)

                        # Install Extension
                    logging.debug("Installing extension")
                    #if gnomeCmd.install(extZipFile):
                    #    logging.info("Installation complete")
                    #else:
                    #    logging.error("Failed to install extension")

                        # Remove Zip file
                    #.remove()

            else:
                logging.debug("extension already installed")


                # Enable/Disable (enable)
            if ext.getEnabled():
                if gnomeCmd.enable(ext.getUuid()):
                    logging.debug("Extension Enabled")
                else:
                    logging.error("Failed to enable extension")
            else:
                if gnomeCmd.disable(ext.getUuid()):
                    logging.debug("Extension Disabled")
                else:
                    logging.error("Failed to disable extension")

                # Settings (dconf)
            #.set()


        logging.info("Sync complete")
