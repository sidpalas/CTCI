# Didn't implement XML objects and methods to test this

tagMap = {'family': '1',
          'person':'2',
          'firstName':'3',
          'lastName':'4',
          'state': '5'}

END = '0'

def encodeXML(rootElement):
    outputBuilder = []
    encodeElement(rootElement,outputBuilder)
    return listToString(outputBuilder)

def encodeElement(element, outputBuilder):
    tag = tagMap([element.name])
    encode(tag, outputBuilder)
    for attribute in element.attributes:
        encodeValue(attribute, outputBuilder)
    encode(END, outputBuilder)
    if not(element.value == None or element.value == ""):
        encodeValue(root.value, outputBuilder)
    else:
        for child in element.children:
            encodeElement(child, outputBuilder)
    encode(END, outputBuilder)

def encodeValue(value, outputBuilder):
    outputBuilder.append(value)
    return

def encodeAttribute(attribute, outputBuilder):
    attributeTag = tagMap[attribute.name]
    encodeValue(attributeTag, outputBuilder)
    attributeVal = attribute.value
    encodeValue(attributeVal, outputBuilder)
    return

def listToString(list):
    return ' '.join(list)
