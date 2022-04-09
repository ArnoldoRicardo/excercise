import json as jsonlib
import xml.etree.cElementTree as ET


def elem_to_dict_tree(elem):
    d = {}

    for subelem in elem:
        v = elem_to_dict_tree(subelem)
        tag = subelem.tag
        value = v[tag]
        try:
            d[tag].append(value)
        except AttributeError:
            d[tag] = [d[tag], value]
        except KeyError:
            d[tag] = value
    text = elem.text
    if d:
        if text:
            d["#text"] = text
    else:
        d = text or None
    return {elem.tag: d}


def elem_to_json(elem):

    if hasattr(elem, "getroot"):
        elem = elem.getroot()
    return jsonlib.dumps(elem_to_dict_tree(elem))


def filter_data(raw_data):
    compact = str(raw_data).replace('\\n', '').replace('  ', '')
    chop = compact.replace("b\'", '').replace("\'", '')

    return chop


def xml2json(file):
    data = ''
    for chunk in file.chunks():
        data += filter_data(chunk)

    elem = ET.fromstring(data)
    return elem_to_json(elem)
