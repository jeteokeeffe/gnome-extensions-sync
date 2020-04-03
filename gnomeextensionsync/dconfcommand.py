import subprocess

class dconfcommand():

    def enabled(self):
        exts = []

        cmd = "dconf read /org/gnome/shell/enabled-extensions"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            #return result.stdout
            for i in result.stdout.strip("[]\n").split(", "):
                exts.append(i.strip("'"))

        return exts


