import configparser, json

BOOLS = {"true": True, "yes": True, "false": False, "no": False}


def coerce(v):
    if v.lower() in BOOLS:
        return BOOLS[v.lower()]
    try:
        return int(v)
    except ValueError:
        return v


cp = configparser.ConfigParser()
cp.read("config.ini")
out = {}
for section in cp.sections():
    node = out
    for part in section.split("."):
        node = node.setdefault(part, {})
    for k, v in cp[section].items():
        node[k] = coerce(v)
json.dump(out, open("config.json", "w"), indent=2)
