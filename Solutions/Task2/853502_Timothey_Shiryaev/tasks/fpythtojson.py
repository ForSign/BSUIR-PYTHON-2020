def classtojsn(obj):
    z = {}

    for i in dir(obj):
        if not i.startswith('_') :
            z[i]=getattr(obj, i)
    return z

def to_json(obj):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return f'"{obj}"'
    elif  isinstance(obj, (tuple, set, list)):
        tuple_set_list = ", ".join(to_json(element) for element in obj)
        return "[" + tuple_set_list + "]"
    elif isinstance(obj, dict):
        pairs = []
        for key, value in obj.items():
            if isinstance(key, (int, float, bool)) or key is None:
                pairs.append("\"" + to_json(key) + "\": " + to_json(value))
            else:
                pairs.append(to_json(key) + ": " + to_json(value))
        result = ", ".join(pair for pair in pairs)
        return "{" + result + "}"
    else: return classtojsn(obj)
