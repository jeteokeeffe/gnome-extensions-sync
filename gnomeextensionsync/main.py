import click
import logging

from .extensioncommand import extensioncommand
from .extensionlist import extensionlist
from .parseinfo import parseinfo
from .parselist import parselist
from .writeconfig import writeconfig
from .readconfig import readconfig
from .dconfcommand import dconfcommand
from .gnomeurl import gnomeurl
from .parsejson import parsejson


@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--conf', default='', help='configuration file')
#@click.option('--dryrun', default=0, help='configuration file')
def generate(conf, verbose):
    """
    Generate a configuration file based on your current extension setup
    """

    configFile = 'gnome-ext.yaml'
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    cmd = extensioncommand()
    logging.debug("gnome-extensions version: {}".format(cmd.version()))
    
        # Get installed extensions
    userparse = parselist(cmd.userlist(), True)
    extList = userparse.getExtensionList()
    #sysparse = parselist(cmd.systemlist())

        # Write Configuration
    logging.debug("Writing configuration file")
    write = writeconfig(configFile)
    write.setExtensionList(extList)
    write.write()
    logging.info("Generate complete")


@cli.command()
@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
def run(conf, dryrun, verbose):
    """
    Run a sync (add/remove) gnome extensions
    """

    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    gnomeCmd = extensioncommand()
    logging.debug("gnome-extensions version: {}".format(gnomeCmd.version()))

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

        logging.info("Found \"{}\" Extension".format(ext.getName()))
            # https://docs.python.org/3/library/tempfile.html

            # Check Extension Exists
        logging.debug("Checking if extension already exists")
        if not installedList.exists(ext.getUuid()):

                # Info on Extension
            output = gnomeurl.info(ext.getUuid())
            pj = parsejson()
            pj.parse(output)
            #.getVersion()
            #.getZipFile()
            extZipFile = "/tmp/jete.zip"
            extVersion = 67

                # Check Compatible for Gnome


                # Download Zip
            logging.info("Downloading extension")
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

@cli.command()
@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
def downloadrun(conf, dryrun, verbose):
    """
    """
    logging.error("to be implemented")

@cli.command()
@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
def download(conf, dryrun, verbose):
    """
    """
    logging.error("to be implemented")

@cli.command()
@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
def upload(conf, dryrun, verbose):
    """
    """
    logging.error("to be implemented")

def main():
    cli()

