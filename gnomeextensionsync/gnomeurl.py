import requests

class gnomeurl():

    def download(uuid, version, temp) -> bool:
        #https://extensions.gnome.org/extension-data/dash-to-dockmicxgx.gmail.com.v67.shell-extension.zip
        uuid = uuid.replace('@','')
        url = "https://extensions.gnome.org/extension-data/{}.v{}.shell-extension.zip".format(uuid, version)
        resp = requests.get(url)
        if resp.status_code == 200:
            open(temp, 'wb').write(resp.content)
        
        return False

    def info(uuid):
        url = "https://extensions.gnome.org/extension-query/?page=1&shell_version=all&search={}".format(uuid)
        resp = requests.get(url)
        print(resp)

        return True
