import os
from video import Video
for x in os.listdir("/home/mary/Bureau/sousleau camra wifi/Mespremiersfilms00100001/"):
    if "VID" in x:
        desc=x[19:-4]
        myfile=x
        Video().create({"name":desc, "filename":myfile})
