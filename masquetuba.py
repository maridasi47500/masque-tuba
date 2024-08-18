import os
from video import Video
for y in "mesdeuxiemefilm Mespremiersfilms00100001 mestroisiemefilm monquatriemefilm".split(" "):
    for x in os.listdir("~/Bureau/sousleau camra wifi/"+y+"/"):
        if "VID" in x:
            desc=x[19:-4]
            myfile=x
            Video().create({"name":desc, "filename":myfile})
