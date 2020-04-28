

class dconfparse():

    def __init__(self):
        self.test = None
        self.settings = []


    def parse(self, output):

        count = 0
        for line in output.split("\n"):
            if not count == 0:
                key = line.split("=")[0]
                value = line.split("=")[1]
                self.settings.append({ key: value})

            count = count + 1
        
        return True

    def getSettings(self):
        return self.settings



d=dconfparse()
d.parse("[/]\nshow-notifications=false\nuser-enabled=false")
print(d.getSettings())
