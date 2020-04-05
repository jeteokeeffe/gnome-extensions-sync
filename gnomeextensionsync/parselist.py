from .extension import extension
from .extensionlist import extensionlist


class parselist():

    STATE_UUID = 1

    def __init__(self, text, manual=False):
        self.extList = extensionlist()
        ext = self.parseextension(text, manual)


    def getExtensionList(self):
        return self.extList


    def parseextension(self, exttext, manual=False):
        count = 0
        ext = extension()

        for line in exttext.split("\n"):
            if count == 0 and len(line.strip()) > 3:
                ext = extension()
                ext.setUuid(line.strip())
                ext.setManualInstall(manual)
                count=count+1
            else:
                if line.startswith("  Name:"):
                    ext.setName(line.split(":")[1].strip())
                elif line.startswith("  URL:"):
                    ext.setURL(line[7:])
                elif line.startswith("  Path:"):
                    ext.setPath(line.split(":")[1].strip())
                elif line.startswith("  Version:"):
                    ext.setVersion(line.split(":")[1].strip())
                elif line.startswith("  State:"):
                    value = line.split(":")[1].strip()
                    if value == "ENABLED":
                        ext.setEnabled(True)

                    self.extList.add(ext)
                    ext = None
                    count = 0
                

        return ext

