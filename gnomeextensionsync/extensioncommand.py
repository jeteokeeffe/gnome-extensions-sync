import subprocess

class extensioncommand():

    def isInstalled(self):
        cmd = "gnome-extensions --version"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        return False

    def version(self):
        cmd = "gnome-extensions --version"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout

    def install(self, zipFile: str):
        cmd = "gnome-extensions install {}".format(zipFile)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True

        print(result.stderr)
        return False


    def remove(self, uuid: str):
        cmd = "gnome-extensions uninstall {}".format(uuid)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def info(self, uuid: str):
        cmd = "gnome-extensions info {}".format(uuid)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout


    def userlist(self):
        cmd = "gnome-extensions list --user --details"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout


    def systemlist(self):
        cmd = "gnome-extensions list --system --details"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout

    def enable(self, uuid: str) -> bool:
        """
        Enable extension
        """
        cmd = "gnome-extensions enable {}".format(uuid)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        return False


    def disable(self, uuid: str) -> bool:
        """
        Disable extension
        """
        cmd = "gnome-extensions disable {}".format(uuid)
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True
        return False
