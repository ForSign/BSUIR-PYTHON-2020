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
        tmp = str_json[1:-1]
        tmp = tmp.split(",")
        result = []
        for i in tmp:
           result.append(from_json(i))

    if str_json[0] == "{":
        result = {}
        tmp = str_json[1:-1]
        tmp = tmp.split(", ")
        for i in tmp:
            tmp1 = i.split(": ")
            tmp1[1] = from_json(tmp1[1])
            tmp1[0] = from_json(tmp1[0])
            result[tmp1[0]] = tmp1[1]

    return result

#print(from_json('"powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]'))

# "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]
# {"James": 9001, "Jo": 3474, "Jess": 11926 }
#{"sammy": {"username": "SammyShark", "location": "Indian Ocean", "online": true, "followers": 987 }, "jesse": { "username": "JesseOctopus", "location": "Pacific Ocean", "online": false, "followers": 432}, "drew": {"username": "DrewSquid", "location": "Atlantic Ocean", "online": false, "followers": 321}, "jamie": {"username": "JamieMantisShrimp", "location": "Pacific Ocean", "online": true, "followers": 654}}

#{ 
#  "sammy" : {
#    "username"  : "SammyShark",
#    "location"  : "Indian Ocean",
#    "online"    : true,
#    "followers" : 987
#  },
#  "jesse" : {
#    "username"  : "JesseOctopus",
#    "location"  : "Pacific Ocean",
#    "online"    : false,
#    "followers" : 432
#  },
#  "drew" : {
#    "username"  : "DrewSquid",
#    "location"  : "Atlantic Ocean",
#    "online"    : false,
#    "followers" : 321
#  },
#  "jamie" : {
#    "username"  : "JamieMantisShrimp",
#    "location"  : "Pacific Ocean",
#    "online"    : true,
#    "followers" : 654
#  }
#}