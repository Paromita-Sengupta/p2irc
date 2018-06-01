import json
from pprint import pprint
from json2html import *

res = {}
with open('json_file.json') as f:
    data = json.load(f)

dict1 = data['p2irc_dev']['mappings']
a = list(dict1.keys())

for x in range(len(a)):

    dict2 = data['p2irc_dev']['mappings'][a[x]]
    b = list(dict2.keys())

    if len(b):
        if 'properties' in b:
            dict3 = data['p2irc_dev']['mappings'][a[x]]['properties']
            p = list(dict3.keys())
            if 'file_metadata' in p:
                dict4 = data['p2irc_dev']['mappings']['file']['properties']['file_metadata']['properties']
                m = list(dict4.keys())
                for i in range(len(m)):
                    p.append(m[i])
                res[a[x]] = p
            else:

                res[a[x]] = p
        else:

            res[a[x]] = p
    else:

        res[a[x]] = p

with open('p2irc.json', 'w') as outfile:
    s = json.dumps(res)
    outfile.write(s)

with open('p2irc.json') as output:
    data1 = json.load(output)

html=json2html.convert(json=data1)

with open("demo.html", "w") as file:
    file.write(html)