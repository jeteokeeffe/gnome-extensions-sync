from .extension import extension

class parseinfo():

    def __init__(self, info):
        self.ext = extension()
        count = 0
        
        for line in info.split("\n"):
            text = line.strip()
            if count == 0:
                self.ext.setUuid(text)
            elif len(text) > 0:
                data = text.split(":")
                if data[0] == 'Name':
                    self.ext.setName(data[1].strip())
                elif data[0] == 'State':
                    self.ext.setState(data[1].strip())
                elif data[0] == 'Description':
                    self.ext.setDescription(data[1].strip())
                elif data[0] == 'Path':
                    self.ext.setPath(data[1].strip())
                elif data[0] == 'URL':
                    data[0] = ''
                    self.ext.setURL("".join(data).strip())
                elif data[0] == 'Version':
                    self.ext.setVersion(data[1].strip())
                #else:
                #    print(data)

            count=count+1

    def getExtension(self):
        return self.ext


