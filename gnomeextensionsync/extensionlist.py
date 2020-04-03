from .extension import extension

class extensionlist:

    def __init__(self):
        self.exts = []

    def add(self, ext: extension):
        self.exts.append(ext)

    def getAll(self):
        return self.exts

    def exists(self, uuid):
        for ext in self.exts:
            print("{} == {}".format(ext.getUuid(), uuid))
            if ext.getUuid() == uuid:
                return True

        return False

    def getCount(self) -> int:
        return self.exts.count()
