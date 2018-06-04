import json
from pprint import pprint
from json2html import *

res = {}
# g=[]
# descrip = {'jkjk'}
# d=list(descrip)
with open('p2irc_file') as f:
    data = json.load(f)

dict1 = data['p2irc_dev']['mappings']
a = list(dict1.keys())

for x in range(len(a)):

    dict2 = data['p2irc_dev']['mappings'][a[x]]
    b = list(dict2.keys())

    if len(b):
        if 'properties' in b:
            dict3 = data['p2irc_dev']['mappings'][a[x]]['properties']
            p = list(list(dict3.keys()))
            if 'file_metadata' in p:
                dict4 = data['p2irc_dev']['mappings']['file']['properties']['file_metadata']['properties']
                m = list(dict4.keys())
                for i in range(len(m)):
                 p.append(m[i])
                res[a[x]] = p

            elif 'doc' in p:
                dict5 = data['p2irc_dev']['mappings']['file']['properties']['doc']['properties']['file_metadata']['properties']
                n = list(dict5.keys())
                for i in range(len(n)):
                    p.append(n[i])
                res[a[x]] = p

            else:
                    res[a[x]] = p
        else:

            res[a[x]] = p
    else:

        res[a[x]] = {}


with open('p2irc_simple_file.json', 'w') as outfile:
    s = json.dumps(res)
    outfile.write(s)

with open('p2irc_simple_file.json') as output:
    data1 = json.load(output)

html=json2html.convert(json=data1)

with open("demo.html", "w") as file:
    file.write(html)