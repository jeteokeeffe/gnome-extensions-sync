import subprocess

class dconfcommand():

    def enabled(self):
        exts = []

        cmd = "dconf read /org/gnome/shell/extensions"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            #return result.stdout
            for i in result.stdout.strip("[]\n").split(", "):
                exts.append(i.strip("'"))

        return exts



    def getSettings(self, uuid):

        name = uuid.split("@")[0]

        cmd = "dconf dump /org/gnome/shell/extensions/{}/".format(name)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout


d=dconfcommand()
d.getSettings('caffeine')
