import json as jsonlib
import xml.etree.cElementTree as ET


def elem_to_dict_tree(elem):
    data = {}

    for subelem in elem:
        v = elem_to_dict_tree(subelem)
        tag = subelem.tag
        value = v[tag]

        try:
            data[tag].append(value)
        except AttributeError:
            data[tag] = [data[tag], value]
        except KeyError:
            data[tag] = value
    text = elem.text
    if data:
        if text:
            data["#text"] = text
    else:
        data = text or ''
    return {elem.tag: data}


def elem_to_dict(elem):

    if hasattr(elem, "getroot"):
        elem = elem.getroot()
    
    data = {}
    tag = elem.tag
    data[tag] = []
    for subelem in elem:
        data[tag].append(elem_to_dict_tree(subelem))

    if not data[tag]:
        data[tag] = ''
    return data

def filter_data(raw_data):
    compact = str(raw_data).replace('\\n', '').replace('  ', '')
    chop = compact.replace("b\'", '').replace("\'", '')

    return chop


def xml2json(file):
    data = ''
    for chunk in file.chunks():
        data += filter_data(chunk)

    elem = ET.fromstring(data)
    return elem_to_dict(elem)
