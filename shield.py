from xml.dom.minidom import parse
import xml.dom.minidom

dom = parse("30675.xml")
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


with open('ed2k.txt', 'w') as f:
    for item in items:
        title = item.getElementsByTagName("title")[0].firstChild.data
        if "S01" in title or "S02" in title:
            if title.endswith('.mkv') and title.startswith("神盾局特工"):
                download_link = get_download_link(item)
                f.write(download_link + '\n')    

        elif "S03" in title:
            if "1024X576" in title and title.startswith("神盾局特工"):
                download_link = get_download_link(item)
                f.write(download_link + '\n')            
        elif "S04" in title or "S05" in title:
            if title.endswith('.mp4') and title.startswith("神盾局特工"):
                download_link = get_download_link(item)
                f.write(download_link + '\n')    
        else:
            if title.startswith("神盾局特工"):
                download_link = get_download_link(item)
                f.write(download_link + '\n')

