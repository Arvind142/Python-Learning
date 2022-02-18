def readProperty(propertyFile):
    map={}
    seprator="="
    with open(propertyFile) as file:
        for line in file:
            if seprator in line:
                key,value = line.split(seprator,1)
                map[key.strip()]=value.strip()
    return map;