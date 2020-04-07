

class extension():

    STATE_ENABLED = "ENABLED"
    STATE_INIT = "INITIALIZED"
    STATE_DISABLED = "DISABLED"

    def __init__(self):
        self.uuid = ""
        self.name = ""
        self.state = ""
        self.version = 0
        self.author = ""
        self.description = ""
        self.name = ""
        self.path = ""
        self.url = ""
        self.isEnabled = False
        self.isManual = False
        self.settings = None

    def setUuid(self, uuid):
        self.uuid = uuid

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setVersion(self, version):
        self.version = version

    def setState(self, state):
        self.state = state

    def setPath(self, path):
        self.path = path

    def setURL(self, url):
        self.url = url

    def setEnabled(self, isEnabled: bool):
        self.isEnabled = isEnabled

    def setManualInstall(self, manual: bool):
        self.isManual = manual

    def setSettings(self, settings):
        self.settings = settings


    def getUuid(self) -> str:
        return self.uuid

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getAuthor(self) -> str:
        return self.author

    def getVersion(self) -> int:
        return self.version

    def getState(self) -> str:
        return self.state

    def getUrl(self) -> str:
        return self.url

    def getPath(self) -> str:
        return self.path

    def getEnabled(self) -> bool:
        return self.isEnabled

    def getManualInstall(self) -> bool:
        return self.isManual

    def getSettings(self):
        return self.settings

