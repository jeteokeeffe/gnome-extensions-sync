import click

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

from gnomeextensionssync.commands.generate import generate as generatecmd
from gnomeextensionssync.commands.run import run as runcmd

@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--conf', default='.config/gnome-extensions-sync/extensions.json', help='configuration file')
#@click.option('--dryrun', default=0, help='configuration file')
def generate(conf, verbose):
    """
    Generate a configuration file based on your current extension setup
    """

    cmd = generatecmd()
    cmd.execute()



@cli.command()
@click.option('-c', '--conf', default='.config/gnome-extensions-sync/extensions.json', help='configuration file')
@click.option('--dryrun', default=0, help='configuration file')
@click.option('-v', '--verbose', is_flag=True)
def run(conf, dryrun, verbose):
    """
    Run a sync (add/remove) gnome extensions
    """
    cmd = runcmd()
    cmd.execute()


#@cli.command()
#@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
#@click.option('--dryrun', default=0, help='configuration file')
#@click.option('-v', '--verbose', is_flag=True)
#def downloadrun(conf, dryrun, verbose):
#    """
#    """
#    logging.error("to be implemented")

#@cli.command()
#@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
#@click.option('--dryrun', default=0, help='configuration file')
#@click.option('-v', '--verbose', is_flag=True)
#def download(conf, dryrun, verbose):
#    """
#    """
#    logging.error("to be implemented")

#@cli.command()
#@click.option('-c', '--conf', default='gnome-ext.yaml', help='configuration file')
#@click.option('--dryrun', default=0, help='configuration file')
#@click.option('-v', '--verbose', is_flag=True)
#def upload(conf, dryrun, verbose):
#    """
#    """
#    logging.error("to be implemented")

def main():
    cli()

