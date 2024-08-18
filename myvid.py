from directory import Directory
class Vid(Directory):
    def __init__(self,name):
        self.name=name
        namevid=name.split(".")[1].lower()
        if namevid == "avi":
            self.vid="x-msvideo"
        else:
            self.vid=namevid
        self.content=open("."+name.replace("%20"," "), 'rb').read()
    def get_name(self):
        return self.name
    def get_html(self):
        return self.content
