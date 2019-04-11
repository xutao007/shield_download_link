from xml.dom.minidom import parse
import xml.dom.minidom

dom = parse("30675.xml")
items = dom.documentElement.getElementsByTagName("channel")[0].getElementsByTagName("item")

with open('ed2k.txt', 'w') as f:
    for item in items:

        title = item.getElementsByTagName("title")[0].firstChild.data
        if title.endswith('.mp4') and title.startswith("神盾局特工"):

            download_link = ""

            ed2k = item.getElementsByTagName("ed2k")[0]
            if ed2k:
                download_link = ed2k.firstChild.data
            else:
                magnet = item.getElementsByTagName("magnet")[0]
                download_link = magnet.firstChild.data

            f.write(download_link + '\n')
