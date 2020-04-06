import json


class parsejson:
    """
    Parse Output from extension-query information
    """

    def __init__(self):
        self.uuid = None
        self.versions = {}
        self.name = None
        self.creator = None
        self.icon = None
        self.screenshot = None
        self.link = None

    def parse(self, output):
        data = json.loads(output)
        if len(data['extensions']) == 1:
            for i in data['extensions']:
                self.uuid = i['uuid']
                self.name = i['name']
                self.creator = i['creator']
                #self.desc = i['description']
                self.icon = i['icon']
                self.link = i['link']
                self.screenshot = i['screenshot']

                for gnomeVersion in i['shell_version_map']:
                    versionArr = []
                    #print("Version: {}".format(gnomeVersion))
                    if type(i['shell_version_map'][gnomeVersion]) == dict:
                        versionArr.append(i['shell_version_map'][gnomeVersion])
                    print(versionArr)
                    self.version = { gnomeVersion : versionArr }

        return False
                
    def getVersions(self):
        return self.versions

    def getName(self):
        return self.name

    def getCreator(self):
        return self.creator

    def getLink(self):
        return self.link

