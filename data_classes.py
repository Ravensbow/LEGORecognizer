import requests
from requests.auth import HTTPDigestAuth
import json
import os
from PIL import Image
from io import BytesIO

key = '51bdc06ad75018be435bbb965fc94840'
mainurl = 'https://rebrickable.com/api/v3/lego/'
kitID = '30434'

def distinct(sequence):
    seen = set()
    for s in sequence:
        if not s in seen:
            seen.add(s)
            yield s

def getPartsList(url):
    myResponse = requests.get(url, params = {'key': key, 'inc_part_details': '1'})
    if(myResponse.ok):
        jData = json.loads(myResponse.content)
    else:
        myResponse.raise_for_status()
    return jData

def partsImportLDRAW():

    url = mainurl + 'sets/' + kitID + '-1/parts/'
    parts = []
    partsList = getPartsList(url)
    for piece in partsList['results']:
        if("LDraw" in piece['part']['external_ids']):
            parts.append(piece['part']['part_num'])
    return parts

def makeLDRAWfile():
    LDRAW_file = open("Data_classes.txt", "w")
    parts = partsImportLDRAW()
    parts = distinct(sorted(parts, key=lambda x:int(x.replace("b",""))))
    for piece in parts:
        line = str(piece)
        LDRAW_file.write(line)
        LDRAW_file.write("\n")
    LDRAW_file.close()

makeLDRAWfile()