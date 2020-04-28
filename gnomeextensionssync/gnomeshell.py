import subprocess

class gnomeshell():

    def __init__(self):
        self.version = None

        self.sessionDesktop = None
        self.sessionType = None

        cmd = "gnome-shell --version"
        result=subprocess.run(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            
            #if result.stdout.beginswith("GNOME Shell"):
            self.version = result.stdout[11:].strip()


    def getCurrentDesktop(self):
        return self.sessionDesktop


    def getSessionType(self):
        return self.sessionType


    def getMajorVersion(self):
        versions = self.version.split(".")[0:2]
        return ".".join(versions)


    def getMinorVersion(self):
        return self.version.split(".")[2] 


    def getVersion(self):
        return self.version
