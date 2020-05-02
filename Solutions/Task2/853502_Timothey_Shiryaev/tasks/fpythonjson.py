import sys

def from_json(str_json):
    if str_json == "null":
        return None

    if str_json == "false":
        return False

    if str_json == "true":
        return True

    try:
        int(str_json)
        result = int(str_json)
    except Exception:
        pass

    try:
        float(str_json)
        result = float(str_json)
    except Exception:
        pass

    if str_json[0] == "\"":
        result = str(str_json).replace('\"','')

    if str_json[0] == "[":
        splitter = str_json[1:-1]
        splitter = splitter.split(",")
        result = []
        for i in splitter:
           result.append(from_json(i))

    if str_json[0] == "{":
        result = {}
        splitter = str_json[1:-1]
        splitter = splitter.split(", ")
        for i in splitter:
            splitter1 = i.split(": ")
            splitter1[0] = from_json(splitter1[0])
            splitter1[1] = from_json(splitter1[1])
            result[splitter1[0]] = splitter1[1]

    return result

print(from_json(input()))

# "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]
# {"James": 9001, "Jo": 3474, "Jess": 11926 }