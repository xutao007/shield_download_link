from xml.dom.minidom import parse
import xml.dom.minidom

dom = parse("30010.xml")
items = dom.documentElement.getElementsByTagName("channel")[0].getElementsByTagName("item")

def get_download_link(item):
    download_link = ""
    ed2k = item.getElementsByTagName("ed2k")
    magnet = item.getElementsByTagName("magnet")
    pan = item.getElementsByTagName('pan')
    if ed2k:
        download_link = ed2k[0].firstChild.data
    elif magnet:
        download_link = magnet[0].firstChild.data
    elif pan:
        download_link = pan[0].firstChild.data
    return download_link

with open('avenger_assemble_download.txt', 'w') as f:
    for item in items:
        title = item.getElementsByTagName("title")[0].firstChild.data
        
        # still need do celete some link by mannul
        if "S01" in title :
            if "1024X576" in title or "720p" in title:
                download_link = get_download_link(item)
                f.write(download_link + '\n') 

        elif "S02" in title:
            if "1280X720" in title or "720p" in title:
                download_link = get_download_link(item)
                f.write(download_link + '\n') 
                    
        elif "S03" in title or "S04" in title or "S05" in title:
            if title.startswith("复仇者集结"):
                download_link = get_download_link(item)
                f.write(download_link + '\n')    